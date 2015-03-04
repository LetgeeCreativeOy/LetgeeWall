# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('private', models.BooleanField(default=False)),
                ('published', models.DateTimeField(auto_now=True)),
                ('logo_url', models.CharField(max_length=256)),
                ('hastag', models.CharField(max_length=32)),
                ('facebook', models.BooleanField(default=True)),
                ('twitter', models.BooleanField(default=True)),
                ('instagram', models.BooleanField(default=True)),
                ('allow_images', models.BooleanField(default=False)),
                ('block_words', models.BooleanField(default=False)),
                ('word_list_url', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
