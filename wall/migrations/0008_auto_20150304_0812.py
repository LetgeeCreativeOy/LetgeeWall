# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0007_auto_20150303_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 4, 8, 12, 0, 907983, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
