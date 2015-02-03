# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'First Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debt_date', models.DateField(auto_now_add=True, verbose_name=b'date')),
                ('customer', models.CharField(max_length=100, verbose_name=b'customer')),
                ('bill', models.PositiveIntegerField(verbose_name=b'bill')),
                ('paid', models.PositiveIntegerField(verbose_name=b'Amount Paid')),
                ('balance', models.PositiveIntegerField(verbose_name=b'balance')),
            ],
            options={
                'verbose_name_plural': 'Debtors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Drug Name')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name=b'quantity')),
                ('unit_cost', models.PositiveIntegerField(default=0, verbose_name=b'Retail Price')),
                ('cost_price', models.PositiveIntegerField(default=0, verbose_name=b'Wholesale Price')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Prescription Drugs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name=b'name')),
                ('unit_cost', models.PositiveIntegerField(default=0, verbose_name=b'Unit Cost')),
            ],
            options={
                'ordering': ['type'],
                'verbose_name_plural': 'Lab Tests',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=100, null=True, verbose_name=b'Customer Name(Optional)', blank=True)),
                ('total_amount', models.PositiveIntegerField(verbose_name=b'Bill')),
                ('full_pay', models.BooleanField(default=True, help_text=b'Please Uncheck if not full payment and enter customer name to keep track of debt', verbose_name=b'Full Payment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name=b'quantity')),
                ('drug_amount', models.PositiveIntegerField(null=True, blank=True)),
                ('item', models.ForeignKey(to='sales.Item')),
                ('sale', models.ForeignKey(to='sales.Sale')),
            ],
            options={
                'verbose_name': 'prescription',
                'verbose_name_plural': 'Purchased Drug Items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sale', models.ForeignKey(to='sales.Sale')),
                ('test', models.ForeignKey(to='sales.LabTest')),
            ],
            options={
                'verbose_name': 'Lab Tests',
                'verbose_name_plural': 'Lab Tests Taken',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'name')),
                ('address', models.CharField(max_length=100, verbose_name=b'address')),
                ('phone', models.CharField(max_length=30, verbose_name=b'Phone Number')),
                ('alternate_phone', models.CharField(max_length=30, verbose_name=b'Alternate Phone Number', blank=True)),
                ('email', models.EmailField(max_length=100, verbose_name=b'Email', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Suppliers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sale',
            name='drugs',
            field=models.ManyToManyField(to='sales.Item', null=True, verbose_name=b'Drugs', through='sales.SaleItem', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sale',
            name='lab_tests',
            field=models.ManyToManyField(to='sales.LabTest', null=True, verbose_name=b'Lab Tests', through='sales.SaleTest', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sale',
            name='processed_by',
            field=models.ForeignKey(verbose_name=b'Processed By', to='clinic.Staff'),
            preserve_default=True,
        ),
    ]
