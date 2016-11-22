# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-22 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_auto_20161118_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractagent',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='type',
            field=models.CharField(choices=[('share.agent', 'agent'), ('share.organization', 'organization'), ('share.institution', 'institution'), ('share.consortium', 'consortium'), ('share.person', 'person')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='type',
            field=models.CharField(choices=[('share.agentrelation', 'agent relation'), ('share.isaffiliatedwith', 'is affiliated with'), ('share.isemployedby', 'is employed by'), ('share.ismemberof', 'is member of')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='related',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='subject',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='type',
            field=models.CharField(choices=[('share.agentrelationversion', 'agent relation version'), ('share.isaffiliatedwithversion', 'is affiliated with version'), ('share.isemployedbyversion', 'is employed by version'), ('share.ismemberofversion', 'is member of version')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='name',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='type',
            field=models.CharField(choices=[('share.agentversion', 'agent version'), ('share.organizationversion', 'organization version'), ('share.institutionversion', 'institution version'), ('share.consortiumversion', 'consortium version'), ('share.personversion', 'person version')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='agent_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='type',
            field=models.CharField(choices=[('share.agentworkrelation', 'agent work relation'), ('share.publisher', 'publisher'), ('share.contributor', 'contributor'), ('share.principalinvestigator', 'principal investigator'), ('share.creator', 'creator'), ('share.host', 'host'), ('share.funder', 'funder')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='agent',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='agent_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='creative_work',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelationversion',
            name='type',
            field=models.CharField(choices=[('share.agentworkrelationversion', 'agent work relation version'), ('share.publisherversion', 'publisher version'), ('share.contributorversion', 'contributor version'), ('share.principalinvestigatorversion', 'principal investigator version'), ('share.creatorversion', 'creator version'), ('share.hostversion', 'host version'), ('share.funderversion', 'funder version')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractcreativework',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractcreativework',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractcreativework',
            name='type',
            field=models.CharField(choices=[('share.creativework', 'creative work'), ('share.presentation', 'presentation'), ('share.dataset', 'data set'), ('share.patent', 'patent'), ('share.poster', 'poster'), ('share.publication', 'publication'), ('share.workingpaper', 'working paper'), ('share.book', 'book'), ('share.conferencepaper', 'conference paper'), ('share.report', 'report'), ('share.project', 'project'), ('share.preprint', 'preprint'), ('share.thesis', 'thesis'), ('share.registration', 'registration'), ('share.dissertation', 'dissertation'), ('share.article', 'article'), ('share.software', 'software')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractcreativeworkversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractcreativeworkversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractcreativeworkversion',
            name='type',
            field=models.CharField(choices=[('share.creativeworkversion', 'creative work version'), ('share.presentationversion', 'presentation version'), ('share.datasetversion', 'data set version'), ('share.patentversion', 'patent version'), ('share.posterversion', 'poster version'), ('share.publicationversion', 'publication version'), ('share.workingpaperversion', 'working paper version'), ('share.bookversion', 'book version'), ('share.conferencepaperversion', 'conference paper version'), ('share.reportversion', 'report version'), ('share.projectversion', 'project version'), ('share.preprintversion', 'preprint version'), ('share.thesisversion', 'thesis version'), ('share.registrationversion', 'registration version'), ('share.dissertationversion', 'dissertation version'), ('share.articleversion', 'article version'), ('share.softwareversion', 'software version')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractworkrelation',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelation',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelation',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelation',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelation',
            name='type',
            field=models.CharField(choices=[('share.workrelation', 'work relation'), ('share.isderivedfrom', 'is derived from'), ('share.documents', 'documents'), ('share.cites', 'cites'), ('share.isidenticalto', 'is identical to'), ('share.compiles', 'compiles'), ('share.issupplementto', 'is supplement to'), ('share.reviews', 'reviews'), ('share.references', 'references'), ('share.ispartof', 'is part of'), ('share.extends', 'extends')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='related',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='subject',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractworkrelationversion',
            name='type',
            field=models.CharField(choices=[('share.workrelationversion', 'work relation version'), ('share.isderivedfromversion', 'is derived from version'), ('share.documentsversion', 'documents version'), ('share.citesversion', 'cites version'), ('share.isidenticaltoversion', 'is identical to version'), ('share.compilesversion', 'compiles version'), ('share.issupplementtoversion', 'is supplement to version'), ('share.reviewsversion', 'reviews version'), ('share.referencesversion', 'references version'), ('share.ispartofversion', 'is part of version'), ('share.extendsversion', 'extends version')], db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='agentidentifier',
            name='agent_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='agentidentifier',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='agentidentifier',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AgentIdentifierVersion'),
        ),
        migrations.AlterField(
            model_name='agentidentifierversion',
            name='agent',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='agentidentifierversion',
            name='agent_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='agentidentifierversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='agentidentifierversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AgentIdentifierVersion'),
        ),
        migrations.AlterField(
            model_name='award',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='award',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AwardVersion'),
        ),
        migrations.AlterField(
            model_name='awardversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='awardversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AwardVersion'),
        ),
        migrations.AlterField(
            model_name='change',
            name='model_type',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='change',
            name='node_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='change',
            name='target_version_type',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='target_version_change', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='extradata',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='extradataversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.TagVersion'),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.TagVersion'),
        ),
        migrations.AlterField(
            model_name='throughawards',
            name='award_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AwardVersion'),
        ),
        migrations.AlterField(
            model_name='throughawards',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughawards',
            name='funder_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='throughawards',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughAwardsVersion'),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='award',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.Award'),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='award_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AwardVersion'),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='funder',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelation'),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='funder_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughAwardsVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributor',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributor',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributor',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughContributorVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributor',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributorversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributorversion',
            name='related',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelation'),
        ),
        migrations.AlterField(
            model_name='throughcontributorversion',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributorversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughContributorVersion'),
        ),
        migrations.AlterField(
            model_name='throughcontributorversion',
            name='subject',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelation'),
        ),
        migrations.AlterField(
            model_name='throughcontributorversion',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='throughsubjects',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='throughsubjects',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughsubjects',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughSubjectsVersion'),
        ),
        migrations.AlterField(
            model_name='throughsubjectsversion',
            name='creative_work',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='throughsubjectsversion',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='throughsubjectsversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughsubjectsversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughSubjectsVersion'),
        ),
        migrations.AlterField(
            model_name='throughtags',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='throughtags',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughtags',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughTagsVersion'),
        ),
        migrations.AlterField(
            model_name='throughtags',
            name='tag_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.TagVersion'),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='creative_work',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughTagsVersion'),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='tag',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.Tag'),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='tag_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.TagVersion'),
        ),
        migrations.AlterField(
            model_name='workidentifier',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='workidentifier',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='workidentifier',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.WorkIdentifierVersion'),
        ),
        migrations.AlterField(
            model_name='workidentifierversion',
            name='creative_work',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='workidentifierversion',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='workidentifierversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='workidentifierversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.WorkIdentifierVersion'),
        ),
        migrations.AlterIndexTogether(
            name='change',
            index_together=set([]),
        ),
    ]
