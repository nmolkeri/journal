# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=1, choices=[(b'B', b'Business'), (b'P', b'Pleasure')])),
                ('international_domestic', models.CharField(max_length=1, choices=[(b'D', b'Domestic'), (b'I', b'International')])),
                ('visit_date', models.DateField()),
                ('attraction', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
