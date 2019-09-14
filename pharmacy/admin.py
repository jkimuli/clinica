from django.contrib import admin
from .models import Supplier,Product,Purchase,Invoice,InvoiceLineItem

# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','alternate_phone','email')
    search_fields = ('name','email')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_date','supplier','product','amount','quantity')
    list_filter = ('purchase_date','supplier','product')
    search_fields = ('supplier','product')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','unit_price','quantity') 

class InvoiceItemAdmin(admin.TabularInline):
    model = InvoiceLineItem       

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_date','customer','status') 
    inlines = [InvoiceItemAdmin]           

