from django.forms import ModelForm
from .models import Supplier,Product,Purchase

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
