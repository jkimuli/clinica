# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visittest',
            name='test',
            field=models.ForeignKey(to='sales.LabTest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visittest',
            name='visit',
            field=models.ForeignKey(to='clinic.Visit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visititem',
            name='item',
            field=models.ForeignKey(to='sales.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visititem',
            name='visit',
            field=models.ForeignKey(to='clinic.Visit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visit',
            name='attendant',
            field=models.ForeignKey(verbose_name=b'attendant', to='clinic.Staff'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visit',
            name='lab_tests',
            field=models.ManyToManyField(to='sales.LabTest', verbose_name=b' Lab Tests', through='clinic.VisitTest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visit',
            name='patient_id',
            field=models.ForeignKey(verbose_name=b'patient', to='clinic.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visit',
            name='prescriptions',
            field=models.ManyToManyField(to='sales.Item', verbose_name=b'Prescriptions', through='clinic.VisitItem'),
            preserve_default=True,
        ),
    ]
