# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='hastag',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='logo_url',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
