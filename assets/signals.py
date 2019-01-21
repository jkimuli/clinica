from django.dispatch import Signal,receiver
#from .models import Asset

service_due = Signal(providing_args=['instance'])

@receiver(service_due)
def run_when_service_due(sender,**kwargs):
    asset = kwargs['instance']
    asset.functional_status = 'SER'

    asset.save()


    



