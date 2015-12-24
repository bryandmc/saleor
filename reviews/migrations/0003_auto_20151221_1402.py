# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20151219_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-review_date']},
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name=b'Display name'),
        ),
    ]
