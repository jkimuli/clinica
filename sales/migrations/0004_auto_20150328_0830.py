# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
        ('sales', '0003_auto_20150326_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.CharField(default=b'Cash Payee', help_text=b'Enter Customer if partial Payment to keep track of debt', max_length=50, blank=True)),
                ('total', models.DecimalField(default=0, verbose_name=b'Amount', editable=False, max_digits=12, decimal_places=2)),
                ('payment', models.DecimalField(verbose_name=b'Amount Paid', max_digits=12, decimal_places=2)),
                ('payment_status', models.CharField(max_length=10, choices=[(b'F', b'Fully Paid'), (b'P', b'Partially Paid')])),
                ('processed_by', models.ForeignKey(verbose_name=b'Processed By', to='clinic.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name=b'Quantity')),
                ('invoice', models.ForeignKey(related_name='items', verbose_name=b'Order', to='sales.Invoice')),
                ('item', models.ForeignKey(verbose_name=b'Item Name', to='sales.Item')),
            ],
            options={
                'verbose_name_plural': 'Item Name',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='debtor',
            name='bill',
            field=models.DecimalField(verbose_name=b'Bill', editable=False, max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
    ]
