# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
    ]
