# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20151221_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='review date'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='display name'),
        ),
    ]
