from django.db import models

# Create your models here.

category_choices = (
    ('DR','Drug'),
    ('LTK','Lab Test Kit'),
    ('CON','Consultation Fee')
)

invoice_status = (
    ('FP','Fully Paid'),
    ('NP','Not Fully Paid'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5,choices=category_choices)
    unit_price = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='Unit Price')
    quantity = models.IntegerField(default=0,verbose_name='Quantity Available')

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_date = models.DateField(auto_now_add = True)
    customer = models.CharField(max_length=100,
                                help_text="Enter a name to keep track of unpaid invoices",
                                default="Cash Paid")
    status = models.CharField(max_length=3,choices=invoice_status)

    @property
    def invoice_total(self):
        #calculate the total amount for the invoice
        total= 0
        for item in self.line_items.all():
            total += item.sub_total
        return total    

class InvoiceLineItem(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="line_items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='+')
    quantity = models.IntegerField()

    @property
    def sub_total(self):
        return self.quantity * self.product.unit_price                

class Purchase(models.Model):
    purchase_date = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='purchases')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()