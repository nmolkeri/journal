# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image1',
            field=models.ImageField(upload_to=b'movies/images/icons/', blank=True),
            preserve_default=True,
        ),
    ]
