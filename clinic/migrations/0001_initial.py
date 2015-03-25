# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name')),
                ('phone', models.CharField(max_length=30, verbose_name=b'Phone')),
                ('alternate_phone', models.CharField(max_length=30, verbose_name=b'Alternate Phone', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email', blank=True)),
                ('designation', models.CharField(max_length=50, verbose_name=b'Designation', choices=[(b'Doctor', b'Doctor'), (b'Nurse', b'Nurse'), (b'Lab Technician', b'Laboratory Technician'), (b'Receptionist', b'Receptionist')])),
            ],
            options={
                'ordering': ['first_name'],
                'verbose_name_plural': 'Employees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name')),
                ('gender', models.CharField(max_length=1, verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.CharField(max_length=100, verbose_name=b'Address', blank=True)),
                ('phone', models.CharField(max_length=30, verbose_name=b'Phone', blank=True)),
                ('dob', models.CharField(help_text=b'Please enter date of birth in format:dd/mm/yy', max_length=30, verbose_name=b'Date of Birth', blank=True)),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name=b'Age')),
            ],
            options={
                'ordering': ['first_name'],
                'verbose_name_plural': 'Patients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=10, verbose_name=b'Visit Type', choices=[(b'IN', b'INPATIENT'), (b'OUT', b'OUTPATIENT')])),
                ('examination', models.TextField(verbose_name=b'Physical Examination')),
                ('diagnosis', models.TextField(verbose_name=b'Diagnosis')),
                ('visit_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Visit Date')),
                ('lab_tests', models.TextField(default=b'None', verbose_name=b' Lab Tests Taken', blank=True)),
                ('prescriptions', models.TextField(default=b'None', verbose_name=b'Prescriptions Required', blank=True)),
                ('attendant', models.ForeignKey(verbose_name=b'Attendant', to='clinic.Employee')),
                ('patient_id', models.ForeignKey(verbose_name=b'Patient', to='clinic.Patient')),
            ],
            options={
                'verbose_name_plural': 'Clinic Visits',
            },
            bases=(models.Model,),
        ),
    ]
