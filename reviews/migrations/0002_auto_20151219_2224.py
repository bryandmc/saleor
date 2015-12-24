# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.CharField(default='nothing', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
