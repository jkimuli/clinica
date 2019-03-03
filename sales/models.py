from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'product_category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    unit_cost = models.DecimalField(default=0,verbose_name='Retail Price',decimal_places=2,max_digits=12)
    description = models.TextField(blank=True,help_text="Product Description")
    type = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',verbose_name='Product Category')
    stock = models.PositiveIntegerField(default=0,blank=True,verbose_name="Available Stock")

    def __str__(self):

        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    address = models.CharField(max_length=100, verbose_name='address')
    phone = models.CharField(max_length=30, verbose_name='Phone Number')
    alternate_phone = models.CharField(max_length=30, verbose_name='Alternate Phone Number', blank=True,null=True)
    email = models.EmailField(max_length=100, verbose_name='Email', blank=True,null=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('supplier_detail', args=[self.pk])

    class Meta:
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

class Order(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    employee = models.ForeignKey('clinic.Employee',on_delete=models.SET_DEFAULT,default="Clinic Attendant",verbose_name='Processed By')
    paid = models.BooleanField(default=False,editable=True,verbose_name="Mark as Fully Paid")
    customer = models.CharField(max_length=100,default='Cash Payment',help_text="Enter Customer name to keep track of debtors")
    order_amount = models.DecimalField(verbose_name='Amount Paid',max_digits=12,decimal_places=2)

    @property
    def total_cost(self):
        return sum(item.sub_total() for item in self.items.all())

    @property
    def balance(self):
        return self.total_cost-self.order_amount    


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items',verbose_name='Product Name')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name= 'Order',related_name='items')
    quantity = models.PositiveSmallIntegerField(default=1,verbose_name='Quantity',help_text='Quantity sold')

    def sub_total(self):
        return self.product.unit_cost * self.quantity

    def __str__(self):
        return '{}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('order_item_detail', args=[self.pk])

    class Meta:
        verbose_name_plural = 'Order Item Particulars'

class Purchase(models.Model):
    created = models.DateField(auto_now_add=True,verbose_name="Date Purchased")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_DEFAULT,default='Unknown Supplier',related_name='items_supplied')
    quantity = models.PositiveIntegerField(default=1,verbose_name='Quantity Purchased')

    def __str__(self):

        return "{} - Quantity {} purchased on {}".format(self.product,self.quantity,self.created)

