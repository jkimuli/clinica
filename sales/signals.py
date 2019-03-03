from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OrderItem,Purchase,Order

@receiver(post_save,sender=OrderItem)
def update_stock(sender,instance,created,**kwargs):
    product = instance.product
    if created:
        product.stock -= instance.quantity

    product.save()

'''@receiver(post_save,sender=Order)
def update_paid_status(sender,instance,created,**kwargs):
    if created:
        if instance.order_amount >= instance.total_cost():
            instance.paid = True
    #instance.save()'''          

@receiver(post_save,sender=Purchase)
def update_stock_on_purchase(sender,instance,created,**kwargs):
    product = instance.product
    if created:
        product.stock +=instance.quantity

    product.save()        


