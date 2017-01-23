# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Not good'), (b'2', b'Below average'), (b'3', b'Average'), (b'4', b'Above average'), (b'5', b'Good')]),
            preserve_default=True,
        ),
    ]
