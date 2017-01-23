# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20160924_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image1',
            field=models.ImageField(default=datetime.datetime(2016, 9, 25, 3, 44, 17, 336519, tzinfo=utc), upload_to=b'images/beerthumbs/'),
            preserve_default=False,
        ),
    ]
