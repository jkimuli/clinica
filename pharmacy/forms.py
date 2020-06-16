from django.forms import ModelForm
from .models import Supplier,Product,Purchase,InvoiceLineItem,Invoice

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'        

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class InvoiceLineItemForm(ModelForm):
    class Meta:
        model = InvoiceLineItem
        exclude=()  

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        exclude=()        

