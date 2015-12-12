# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buzzfeed', '0002_auto_20151126_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buzzfeedsearch',
            name='user',
        ),
        migrations.AddField(
            model_name='buzzfeedsearch',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 12, 12, 13, 39, 0, 962860, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
