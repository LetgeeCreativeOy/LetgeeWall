# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0006_auto_20150303_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='hastag',
            new_name='hashtag',
        ),
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 12, 29, 33, 880557, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
