# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141108_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='publish',
            new_name='published',
        ),
    ]
