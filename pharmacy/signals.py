from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase,Product

@receiver(post_save,sender=Purchase)
def add_quantity_on_purchase(sender,instance,**kwargs):
    product = instance.product
    product.quantity += instance.quantity
    product.save()