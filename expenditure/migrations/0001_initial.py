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
                ('amount', models.DecimalField(verbose_name=b'Amount', max_digits=12, decimal_places=2)),
                ('incurred_by', models.ForeignKey(verbose_name=b'Employee Name', to='clinic.Employee')),
            ],
            options={
                'verbose_name_plural': 'Expenses',
            },
            bases=(models.Model,),
        ),
    ]
