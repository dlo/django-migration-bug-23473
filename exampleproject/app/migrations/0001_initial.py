# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import exampleproject.app.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True, error_messages={b'invalid': exampleproject.app.models.IgnoreFormatString(b'Err, this is invalid.')})),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
