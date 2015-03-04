# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_auto_20150303_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='event',
            field=models.ForeignKey(default=0, to='wall.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 11, 53, 44, 525155, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
