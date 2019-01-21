__author__ = 'julius'

from django.contrib import admin
from .models import Category,Product,Order, OrderItem, Supplier,Debtor,Purchase


class CategoryAdmin(admin.ModelAdmin):
	fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'unit_cost','stock')
    search_fields = ('name', 'type')
    list_filter = ('type',)

class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address', 'phone', 'alternate_phone', 'email',)

class DebtorAdmin(admin.ModelAdmin):

    def has_add_permission(self,request):
        return False

    #search_fields = ('name',)
    list_display = ('created','debt_status','debt_amount')    

class PurchaseAdmin(admin.ModelAdmin):
    search_fields = ('product','supplier')
    list_filter=('supplier','product')
    list_display = ('created','product','supplier','quantity')  

class OrderItemInlineAdmin(admin.TabularInline):
    model = OrderItem
    extra = 2

class OrderAdmin(admin.ModelAdmin):
	inlines = [OrderItemInlineAdmin,]
	date_hierarchy = 'created'
	list_display = ('created','employee','customer','total_cost','paid','order_amount')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Debtor,DebtorAdmin)
admin.site.register(Purchase,PurchaseAdmin)

