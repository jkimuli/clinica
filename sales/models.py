from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

PRODUCT_CATEGORIES = (

    ('FEE', 'CLINICAL FEES'),
    ('TEST', 'LAB_TESTS'),
    ('DRUG', 'PRESCRIPTION DRUG'),
)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    processed_by = models.ForeignKey('clinic.Employee', verbose_name='Processed By')
    total = models.DecimalField(default=0, verbose_name="Amount",decimal_places=2,max_digits=12,editable=False)

    '''def item_names(self):
        """return items for a given order"""

        return ','.join([a.name for a in self.items.all()])

    #Calculating total order amount from the subtotals from each order item

    def total_amount(self):

        amount = 0

        for a in self.items.all():
            amount += a.sub_total

        return amount

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.total = self.total_amount()

    item_names.short_description = 'Order Items'''''


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Item Name')
    unit_cost = models.DecimalField(default=0,verbose_name='Retail Price',decimal_places=2,max_digits=12)
    type = models.CharField(max_length=10, choices=PRODUCT_CATEGORIES, verbose_name='Item Category')

    def __unicode__(self):

        return u'%s' % self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, verbose_name='Item Name')
    order_id = models.ForeignKey(Order,verbose_name= 'Order')
    quantity = models.PositiveSmallIntegerField(default=1,verbose_name='Quantity')

    @property
    def sub_total(self):

        return self.item.unit_cost * self.quantity

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Item Name'


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    address = models.CharField(max_length=100, verbose_name='address')
    phone = models.CharField(max_length=30, verbose_name='Phone Number')
    alternate_phone = models.CharField(max_length=30, verbose_name='Alternate Phone Number', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email', blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('supplier_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Suppliers'
        ordering = ['name']


class Debtor(models.Model):
    debt_date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    customer = models.CharField(max_length=100,verbose_name='Customer')
    order = models.ForeignKey(Order,verbose_name='Order')
    bill = models.DecimalField(verbose_name='Bill',max_digits=12,decimal_places=2)
    paid = models.DecimalField(verbose_name='Amount Paid',max_digits=12,decimal_places=2)
    balance = models.DecimalField(verbose_name='Balance',max_digits=12,decimal_places=2,editable=False)

    class Meta:
        verbose_name_plural = 'Debtors'



