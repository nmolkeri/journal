# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20161018_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='international_domestic',
            field=models.CharField(max_length=15, choices=[(b'Domestic', b'Domestic'), (b'International', b'International')]),
            preserve_default=True,
        ),
    ]
