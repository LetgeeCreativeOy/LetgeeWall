# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=140)),
                ('sender', models.CharField(max_length=32)),
                ('service', models.CharField(default=b'THIS', max_length=16, choices=[(b'THIS', b'THIS'), (b'FACEBOOK', b'FACEBOOK'), (b'TWITTER', b'TWITTER'), (b'INSTAGRAM', b'INSTAGRAM')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
