
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.urls import reverse,reverse_lazy

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

STAFF_DESIGNATION = (
    ('DR', 'Doctor'),
    ('NR', 'Nurse'),
    ('LT', 'Laboratory Technician'),
    ('RR', 'Receptionist'),
)

CLINIC_TYPE = (
    ('IN', 'INPATIENT'),
    ('OUT', 'OUTPATIENT'),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gender')
    address = models.CharField(max_length=100, blank=True,null=True,verbose_name='Address')
    phone = models.CharField(max_length=30, blank=True,null=True,verbose_name='Phone')
    dob = models.CharField(max_length=30, verbose_name='Date of Birth', help_text='Please enter date of birth in format:dd/mm/yy', blank=True,null=True)
    age = models.PositiveSmallIntegerField(default=1,verbose_name='Age')

    class Meta:
        verbose_name_plural = 'Patients'
        ordering = ['first_name']

    def __str__(self):

        return '{}  {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('patient-detail', args=[self.pk])

    @property
    def get_full_name(self):
        """returns the person's full name"""

        return '{}  {}'.format(self.first_name, self.last_name)

class Employee(AbstractUser):
    phone = models.CharField(max_length=30,verbose_name='Phone')
    alternate_phone = models.CharField(max_length=30,blank=True,null=True,verbose_name='Alternate Phone')
    designation = models.CharField(max_length=2,choices=STAFF_DESIGNATION,verbose_name='Designation')

    class Meta:
        verbose_name_plural = 'Employees'
        
    def get_absolute_url(self):
        return reverse('staff-detail', args=[self.pk])

    def __str__(self):

        return '{}  {}'.format(self.first_name, self.last_name)

class Visit(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,verbose_name="Patient",related_name='patient_history')
    category = models.CharField(max_length=4, choices=CLINIC_TYPE,verbose_name="Visit Type")
    examination = models.TextField(verbose_name='Physical Examination Carried Out')
    diagnosis = models.TextField(verbose_name="Diagnosis")
    attendant = models.ForeignKey(Employee,on_delete=models.SET_DEFAULT,default='Unknown Employee',verbose_name='Attendant',related_name='visits_handled')
    visit_date = models.DateField(auto_now_add=True, verbose_name="Visit Date")
    lab_tests = models.TextField(verbose_name=' Lab Tests Taken',blank=True,default="None")
    prescriptions = models.TextField(verbose_name='Prescriptions Required',blank=True,default="None")

    class Meta:
        verbose_name_plural = 'Clinic Visits'







