# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='debtor',
            name='order',
            field=models.ForeignKey(default=1, verbose_name=b'Order', to='sales.Order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='debtor',
            name='balance',
            field=models.DecimalField(verbose_name=b'Balance', editable=False, max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='debtor',
            name='bill',
            field=models.DecimalField(verbose_name=b'Bill', max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='debtor',
            name='customer',
            field=models.CharField(max_length=100, verbose_name=b'Customer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='debtor',
            name='paid',
            field=models.DecimalField(verbose_name=b'Amount Paid', max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='processed_by',
            field=models.ForeignKey(verbose_name=b'Processed By', to='clinic.Employee'),
            preserve_default=True,
        ),
    ]
