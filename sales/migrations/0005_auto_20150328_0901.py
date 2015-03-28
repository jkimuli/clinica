# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20150328_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtor',
            name='order',
            field=models.ForeignKey(verbose_name=b'Order', to='sales.Invoice'),
            preserve_default=True,
        ),
    ]
