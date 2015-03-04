# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_auto_20150303_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='logo_url',
            field=models.CharField(default=b'', max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='word_list_url',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
