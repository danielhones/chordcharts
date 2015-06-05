# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_charts', '0002_remove_chordchart_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chordchart',
            name='album',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='chordchart',
            name='artist',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
    ]
