# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='international_domestic',
            field=models.CharField(max_length=12, choices=[(b'Domestic', b'Domestic'), (b'International', b'International')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='reason',
            field=models.CharField(max_length=10, choices=[(b'Business', b'Business'), (b'Pleasure', b'Pleasure')]),
            preserve_default=True,
        ),
    ]
