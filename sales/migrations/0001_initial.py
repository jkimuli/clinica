# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debt_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date')),
                ('customer', models.CharField(max_length=100, verbose_name=b'customer')),
                ('bill', models.PositiveIntegerField(verbose_name=b'Bill')),
                ('paid', models.PositiveIntegerField(verbose_name=b'Amount Paid')),
                ('balance', models.PositiveIntegerField(verbose_name=b'Balance')),
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
                ('name', models.CharField(max_length=100, verbose_name=b'Item Name')),
                ('unit_cost', models.DecimalField(default=0, verbose_name=b'Retail Price', max_digits=12, decimal_places=2)),
                ('type', models.CharField(max_length=10, verbose_name=b'Item Category', choices=[(b'FEE', b'CLINICAL FEES'), (b'TEST', b'LAB_TESTS'), (b'DRUG', b'PRESCRIPTION DRUG')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(default=0, verbose_name=b'Amount', editable=False, max_digits=12, decimal_places=2)),
                ('processed_by', models.ForeignKey(verbose_name=b'Employee Name', to='clinic.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name=b'Quantity')),
                ('item', models.ForeignKey(verbose_name=b'Item Name', to='sales.Item')),
                ('order_id', models.ForeignKey(verbose_name=b'Order', to='sales.Order')),
            ],
            options={
                'verbose_name_plural': 'Item Name',
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
    ]
