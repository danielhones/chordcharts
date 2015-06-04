# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChordChart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('artist', models.CharField(default=b'', max_length=255)),
                ('album', models.CharField(default=b'', max_length=255)),
                ('plain_text', models.TextField(default=b'')),
                ('json', models.TextField(default=b'')),
            ],
        ),
    ]
