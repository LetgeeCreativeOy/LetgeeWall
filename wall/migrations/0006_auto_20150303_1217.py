# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_auto_20150303_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url_name',
            field=models.CharField(default=b'', max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 12, 17, 26, 259039, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
