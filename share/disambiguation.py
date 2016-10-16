from django.core.exceptions import ValidationError

from share import models

__all__ = ('GraphDisambiguator', )


class GraphDisambiguator:
    def __init__(self):
        self.__disambiguator_map = {}
        self._gather_disambiguators(Disambiguator)

    def disambiguate(self, change_graph):
        nodes = sorted(change_graph.nodes, key=self._disambiguweight, reverse=True)
        for n in nodes:
            n.update_relations(change_graph.node_map)
            if n.is_merge:
                continue
            instance = self.instance_for_node(n)
            if isinstance(instance, list):
                # TODO after merging is fixed, add mergeaction change to graph
                raise NotImplementedError()
            else:
                n.instance = instance
            for ref in n.refs:
                change_graph.node_map[ref] = n

    def instance_for_node(self, node):
        NodeDisambiguator = self.__disambiguator_map.get(node.model._meta.concrete_model, GenericDisambiguator)
        return NodeDisambiguator(node.id, node.resolved_attrs, node.model).find()

    def _disambiguweight(self, node):
        # Models with exactly 1 foreign key field (excluding those added by
        # ShareObjectMeta) are disambiguated first, because they might be used
        # to uniquely identify the object they point to. Then do the models with
        # 0 FKs, then 2, 3, etc.
        ignored = {'same_as', 'extra'}
        fk_count = sum(1 for f in node.model._meta.get_fields() if f.editable and (f.many_to_one or f.one_to_one) and f.name not in ignored)
        return fk_count if fk_count == 1 else -fk_count

    def _gather_disambiguators(self, base):
        for cls in base.__subclasses__():
            for_model = getattr(cls, 'FOR_MODEL', None)
            if for_model:
                self.__disambiguator_map[for_model] = cls
            self._gather_disambiguators(cls)


class Disambiguator():

    def __init__(self, id, attrs, model):
        self.id = id
        self.model = model
        # only include attrs with truthy values
        self.attrs = {k: v for k, v in attrs.items() if v}
        self.is_blank = isinstance(id, str) and id.startswith('_:')

    def disambiguate(self):
        raise NotImplementedError()

    def find(self):
        if self.id and not self.is_blank:
            return self.model._meta.concrete_model.objects.get(pk=self.id)
        return self.disambiguate()


class GenericDisambiguator(Disambiguator):

    @property
    def is_through_table(self):
        # TODO fix this...
        return 'Through' in self.model.__name__ or self.model._meta.concrete_model in {
            models.EntityWorkRelation,
            models.AbstractEntityRelation,
            models.AbstractWorkRelation,
        }

    def disambiguate(self):
        if not self.attrs:
            return None

        if self.is_through_table:
            return self._disambiguate_through()

        return self.model.objects.filter(**self.attrs).first()

    def _disambiguate_through(self):
        fields = [
            f for f in self.model._meta.get_fields()
            if f.is_relation and f.editable and f.name not in {'same_as', 'extra'}
        ]
        # Don't dissambiguate through tables that don't have both sides filled out
        for field in fields:
            if field.name not in self.attrs:
                return None

        try:
            return self.model.objects.get(**{field.name: self.attrs[field.name] for field in fields})
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned):
            return None


class UniqueAttrDisambiguator(Disambiguator):
    @property
    def unique_attr(self):
        raise NotImplementedError()

    def not_found(self):
        return None

    def disambiguate(self):
        value = self.attrs.get(self.unique_attr)
        if not value:
            return None
        try:
            query = {self.unique_attr: value}
            return self.model.objects.get(**query)
        except self.model.DoesNotExist:
            return self.not_found()


class WorkIdentifierDisambiguator(UniqueAttrDisambiguator):
    FOR_MODEL = models.WorkIdentifier
    unique_attr = 'uri'


class EntityIdentifierDisambiguator(UniqueAttrDisambiguator):
    FOR_MODEL = models.EntityIdentifier
    unique_attr = 'uri'


class TagDisambiguator(UniqueAttrDisambiguator):
    FOR_MODEL = models.Tag
    unique_attr = 'name'


class SubjectDisambiguator(UniqueAttrDisambiguator):
    FOR_MODEL = models.Subject
    unique_attr = 'name'

    def not_found(self):
        raise ValidationError('Invalid subject: {}'.format(self.attrs['name']))


class AbstractEntityDisambiguator(Disambiguator):
    FOR_MODEL = models.AbstractEntity

    def disambiguate(self):
        entities = []
        for id in self.attrs.get('entityidentifiers', ()):
            try:
                identifier = models.EntityIdentifier.objects.get(id=id)
                entities.append(identifier.entity)
            except models.EntityIdentifier.DoesNotExist:
                pass
        if not entities:
            return None
        elif len(entities) == 1:
            return entities[0]
        else:
            return entities


class AbstractCreativeWorkDisambiguator(Disambiguator):
    FOR_MODEL = models.AbstractCreativeWork

    def disambiguate(self):
        works = []
        for id in self.attrs.get('workidentifiers', ()):
            try:
                identifier = models.WorkIdentifier.objects.get(id=id)
                works.append(identifier.creative_work)
            except models.WorkIdentifier.DoesNotExist:
                pass
        if not works:
            return None
        elif len(works) == 1:
            return works[0]
        else:
            return works
