# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.BigIntegerField(blank=True, db_index=True, help_text="Scopus's auid", null=True)),
                ('initials', models.CharField(default='', max_length=20)),
                ('surname', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0, help_text='1 for first author, etc. Can have multiple Authorship entries for one value of order.')),
                ('affiliation_id', models.IntegerField(db_index=True, help_text="Scopus's afid", null=True)),
                ('organization', models.CharField(db_index=True, default='', help_text='Name from 1st organization node in affiliation details', max_length=300)),
                ('department', models.CharField(default='', help_text='Name from 2nd organization node in affiliation details', max_length=200)),
                ('country', models.CharField(max_length=10)),
                ('city', models.CharField(help_text='Not currently stored', max_length=30)),
            ],
            options={
                'db_table': 'authorship',
            },
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cite_to', models.BigIntegerField(db_index=True, default=-1, help_text='EID of document being cited')),
                ('cite_from', models.BigIntegerField(db_index=True, default=-1, help_text='EID (or group ID?) of citing document')),
            ],
            options={
                'db_table': 'citation',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('eid', models.BigIntegerField(db_index=True, help_text='A unique identifier for the record; but see group_id', primary_key=True, serialize=False)),
                ('doi', models.CharField(help_text='DOI', max_length=150, null=True)),
                ('pub_year', models.IntegerField(db_index=True, default=-1, help_text='Publication year recorded in xocs:pub-year, backing off to xocs:sort-year where pub-year is unavailable')),
                ('group_id', models.BigIntegerField(blank=True, db_index=True, help_text='An EID shared by likely duplicate doc entries', null=True)),
                ('title', models.CharField(help_text='The original (untranslated) title', max_length=400)),
                ('citation_count', models.IntegerField(default=0, help_text='Citation count from citedby.xml')),
                ('title_language', models.CharField(default='', help_text='The language of the original title', max_length=5)),
                ('abstract', models.CharField(default='', help_text='Abstract is not currently imported', max_length=1000)),
                ('citation_type', models.CharField(choices=[('ab', 'ab = Abstract Report'), ('ar', 'ar = Article'), ('ba', 'ba'), ('bk', 'bk = Book'), ('br', 'br = Book Review'), ('bz', 'bz = Business Article'), ('cb', 'cb = Conference Abstract'), ('ch', 'ch = Chapter'), ('cp', 'cp = Conference Paper'), ('cr', 'cr = Conference Review'), ('di', 'di = Dissertation'), ('ed', 'ed = Editorial'), ('er', 'er = Erratum'), ('ip', 'ip = Article in Press'), ('le', 'le = Letter'), ('no', 'no = Note'), ('pa', 'pa = Patent'), ('pr', 'pr = Press Release'), ('re', 're = Review'), ('rf', 'rf'), ('rp', 'rp = Report'), ('sh', 'sh = Short Survey'), ('wp', 'wp = Working Paper')], default='', help_text='The type of document', max_length=5)),
            ],
            options={
                'db_table': 'document',
            },
        ),
        migrations.CreateModel(
            name='ItemID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(db_index=True, help_text='The identifier', max_length=20)),
                ('item_type', models.CharField(help_text='ItemID type (see Scopus documentation)', max_length=40)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scopus.Document')),
            ],
            options={
                'db_table': 'itemid',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scopus_source_id', models.BigIntegerField(db_index=True, default=-1, help_text="Scopus's srcid")),
                ('source_type', models.CharField(choices=[('b', 'b = Book'), ('d', 'd = Trade Journal'), ('j', 'j = Journal'), ('k', 'k = Book Series'), ('m', 'm = Multi-volume Reference Works'), ('p', 'p = Conference Proceeding'), ('r', 'r = Report'), ('n', 'n = Newsletter'), ('w', 'w = Newspaper')], db_index=True, help_text='Source type', max_length=1, null=True)),
                ('source_title', models.CharField(max_length=350)),
                ('source_abbrev', models.CharField(max_length=150)),
                ('issn_print', models.CharField(db_index=True, max_length=15, null=True)),
                ('issn_electronic', models.CharField(db_index=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'source',
            },
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('scopus_source_id', 'issn_print', 'issn_electronic')]),
        ),
        migrations.AddField(
            model_name='document',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Where the document is published', null=True, on_delete=django.db.models.deletion.CASCADE, to='Scopus.Source'),
        ),
        migrations.AddField(
            model_name='authorship',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scopus.Document'),
        ),
    ]
