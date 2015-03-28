# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20150325_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='items', default=1, verbose_name=b'Order', to='sales.Order'),
            preserve_default=False,
        ),
    ]
