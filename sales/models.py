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

    FULLY_PAID = 0
    PARTIAL_PAID = 1
    NOT_PAID = 2

    ORDER_STATUS = (
     (FULLY_PAID,'Fully Paid'),
     (PARTIAL_PAID, 'Partially Paid'),
     (NOT_PAID, 'Not Paid'),
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey('clinic.Employee',on_delete=models.SET_DEFAULT,default="Clinic Attendant",verbose_name='Processed By')
    paid = models.PositiveSmallIntegerField(choices=ORDER_STATUS,editable=False,default=NOT_PAID)
    customer = models.CharField(max_length=100,default='Cash Payment',help_text="Enter Customer name to keep track of debtors")
    order_amount = models.DecimalField(verbose_name='Amount Paid',max_digits=12,decimal_places=2)

    def total_cost(self):
        return sum(item.sub_total() for item in self.items.all())

    def save(self,*args,**kwargs):
        
        super(Order,self).save(*args,**kwargs)  

        if self.pk:
            #set the paid status based on the order_amount and the total cost of the order 
            if self.order_amount == self.total_cost():
                # order is fully paid
                self.paid = Order.FULLY_PAID
            elif self.order_amount == 0:
                self.paid = Order.NOT_PAID
            else:
                self.paid = Order.PARTIAL_PAID

            super(Order,self).save(*args,**kwargs)    

        # Create a new Debtor in the database depending on the value of self.paid

        if (self.paid==Order.NOT_PAID) or (self.paid==Order.PARTIAL_PAID):
            amount = self.total_cost() - self.order_amount
            debtor = Debtor()
            debtor.debt_amount = amount
            debtor.order = self
            debtor.save()       
        

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

class Debtor(models.Model):
    created = models.DateField(auto_now_add=True,verbose_name="Date")
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    clear_debt = models.BooleanField(default=False)
    debt_amount = models.DecimalField(max_digits=12,decimal_places=2,verbose_name="Debt Amount",editable=False)

    class Meta:
        verbose_name_plural = "Debtors"    

    @property
    def debt_status(self):
        if not self.clear_debt:
              return "Debt Outstanding"

    def save(self,*args,**kwargs):
        super(Debtor,self).save(*args,**kwargs)

        if self.pk and self.clear_debt:
            # if clear_debt is set to True , remove the specific object from the list of debtors
            debtor = Debtor.objects.filter(pk=self.pk)
            debtor.delete()
                
