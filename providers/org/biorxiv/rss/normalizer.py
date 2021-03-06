from share.normalize import ctx
from share.normalize import tools
from share.normalize.parsers import Parser


class WorkIdentifier(Parser):
    uri = tools.IRI(ctx)


class Organization(Parser):
    schema = tools.GuessAgentType(ctx, default='Organization')
    name = ctx


class Publisher(Parser):
    agent = tools.Delegate(Organization, ctx)


class Person(Parser):
    given_name = tools.ParseName(ctx).first
    family_name = tools.ParseName(ctx).last
    additional_name = tools.ParseName(ctx).middle
    suffix = tools.ParseName(ctx).suffix


class Creator(Parser):
    order_cited = ctx('index')
    agent = tools.Delegate(Person, ctx)
    cited_as = ctx


class Subject(Parser):
    name = ctx


class ThroughSubjects(Parser):
    subject = tools.Delegate(Subject, ctx)


class Preprint(Parser):
    title = ctx.item['dc:title']
    description = ctx.item.description
    date_published = tools.ParseDate(ctx.item['dc:date'])
    date_updated = tools.ParseDate(ctx.item['dc:date'])

    subjects = tools.Map(
        tools.Delegate(ThroughSubjects),
        tools.Concat(tools.Static('Biology and life sciences'))
    )

    identifiers = tools.Map(tools.Delegate(WorkIdentifier), ctx.item['dc:identifier'])

    related_agents = tools.Concat(
        tools.Delegate(Publisher, ctx.item['dc:publisher']),
        tools.Map(tools.Delegate(Creator), ctx.item['dc:creator']),
    )
