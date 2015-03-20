
from django.db import models
import datetime
from django.core.urlresolvers import reverse,reverse_lazy

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

STAFF_DESIGNATION = (
    ('Doctor', 'Doctor'),
    ('Nurse', 'Nurse'),
    ('Lab Technician', 'Laboratory Technician'),
    ('Receptionist', 'Receptionist'),
)

CLINIC_TYPE = (
    ('IN', 'INPATIENT'),
    ('OUT', 'OUTPATIENT'),
)

FUNCTIONAL_STATUS = (
    ('NEW', 'NEWLY ACQUIRED'),
    ('GOOD', 'GOOD WORKING CONDITION'),
    ('REPAIR', 'DUE FOR SERVICE'),
    ('UNREPAIRABLE', 'UNREPAIRABLE'),
)


class Patient(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gender')
    address = models.CharField(max_length=100, blank=True, verbose_name='Address')
    phone = models.CharField(max_length=30, blank=True, verbose_name='Phone')
    dob = models.CharField(max_length=30, verbose_name='Date of Birth', help_text='Please enter date of birth in format:dd/mm/yy', blank=True)
    age = models.PositiveSmallIntegerField(default=0,verbose_name='Age')

    class Meta:
        verbose_name_plural = 'Patients'
        ordering = ['first_name']

    def __unicode__(self):

        return u'%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    def _get_full_name(self):
        """returns the person's full name"""

        return '%s  %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)


class Employee(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='First Name')
    last_name = models.CharField(max_length=30,verbose_name='Last Name')
    phone = models.CharField(max_length=30,verbose_name='Phone')
    alternate_phone = models.CharField(max_length=30,blank=True,verbose_name='Alternate Phone')
    email = models.EmailField(blank=True,verbose_name='Email')
    designation = models.CharField(max_length=50,choices=STAFF_DESIGNATION,verbose_name='Designation')

    class Meta:
        verbose_name_plural = 'Employees'
        ordering =['first_name']

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})

    def __unicode__(self):

        return u'%s %s' % (self.first_name, self.last_name)

    def _get_full_name(self):
        """ returns the person's full name """

        return u'%s  %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)


class Visit(models.Model):
    patient_id = models.ForeignKey(Patient, verbose_name="Patient")
    category = models.CharField(max_length=10, choices=CLINIC_TYPE, verbose_name="Visit Type")
    examination = models.TextField(verbose_name='Physical Examination')
    diagnosis = models.TextField(verbose_name="Diagnosis")
    attendant = models.ForeignKey(Employee, verbose_name='Attendant')
    visit_date = models.DateTimeField(auto_now_add=True, verbose_name="Visit Date")
    lab_tests = models.TextField(verbose_name=' Lab Tests Taken',blank=True,default="None")
    prescriptions = models.TextField(verbose_name='Prescriptions Required',blank=True,default="None")

    class Meta:
        verbose_name_plural = 'Clinic Visits'







