# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expense_date', models.DateField(auto_now_add=True, verbose_name=b'Date Expense Incurred')),
                ('particulars', models.TextField(verbose_name=b'Particulars')),
                ('amount', models.PositiveIntegerField(verbose_name=b'Amount')),
                ('incurred_by', models.ForeignKey(to='clinic.Staff')),
            ],
            options={
                'verbose_name_plural': 'Expenses',
            },
            bases=(models.Model,),
        ),
    ]
