from django.db import models
from datetime import datetime,timedelta,date

from django.urls import reverse,reverse_lazy
from .signals import service_due

# Create your models here.

ASSET_INVENTORY = (
    ('MED', 'MEDICAL'),
    ('ELE', 'ELECTRO-MECHANICAL'),
    ('FUN', 'FURNITURE'),
)

FUNCTIONAL_STATUS = (
    ('GD', 'GOOD WORKING CONDITION'),
    ('SER', 'DUE FOR SERVICE'),
    ('DOWN', 'UNREPAIRABLE'),
)

class Asset(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    category = models.CharField(max_length=5, choices=ASSET_INVENTORY, verbose_name='category')
    acquired_on = models.DateField( verbose_name='Equipment Registration Date')
    functional_status = models.CharField(max_length=6,choices=FUNCTIONAL_STATUS,default='GD')
    service_interval = models.PositiveIntegerField(verbose_name='Service Interval', null=True,
             help_text='Service Interval in days for machine that requires service',blank=True
            )
    last_service_date = models.DateField(verbose_name='Last Service Date', blank=True,
            help_text='Last Service date for serviceable machine',null=True
        )

  
    def __str__(self):

        return "{} - {}".format(self.name, self.category)

    def get_absolute_url(self):
        return reverse('asset_detail', args=[self.pk])
    
    def service_status(self):
        is_due_for_service = 'No Servicing Required'

        if not self.last_service_date is None and not self.service_interval is None:
            if (self.last_service_date +  timedelta(self.service_interval)) < date.today():
            
                self.functional_status = 'SER'
                is_due_for_service = 'Service Pending'

            else:
                is_due_for_service = 'Service OK'
                
            self.save() 

        return is_due_for_service    

    class Meta:
        verbose_name_plural = 'Fixed Asset Register'

 





