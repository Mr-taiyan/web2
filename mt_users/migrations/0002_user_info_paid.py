# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mt_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='paid',
            field=models.BooleanField(default=b'false'),
        ),
    ]
