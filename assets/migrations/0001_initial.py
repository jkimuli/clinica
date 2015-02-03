# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'name')),
                ('category', models.CharField(max_length=100, verbose_name=b'category', choices=[(b'MEDICAL', b'MEDICAL'), (b'ELECTRO', b'ELECTRO-MECHANICAL'), (b'FURNITURE', b'FURNITURE')])),
                ('acquired_on', models.DateField(verbose_name=b'Equipment Delivery Date')),
                ('service_period', models.PositiveIntegerField(verbose_name=b'Service Interval')),
                ('last_service_date', models.DateField(verbose_name=b'Last Service Date', blank=True)),
                ('service_due', models.BooleanField(default=False, verbose_name=b'Due for Service?')),
            ],
            options={
                'verbose_name': 'asset',
                'verbose_name_plural': 'Fixed Assets',
            },
            bases=(models.Model,),
        ),
    ]
