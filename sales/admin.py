__author__ = 'julius'

from django.contrib import admin
from .models import Item, Order, OrderItem, Supplier, Debtor


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'unit_cost',)
    search_fields = ('name',)


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address', 'phone', 'alternate_phone', 'email',)


class OrderItemInlineAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1

class DebtorInlineAdmin(admin.TabularInline):
	model = Debtor
	extra = 1


class OrderAdmin(admin.ModelAdmin):

    inlines = [OrderItemInlineAdmin,DebtorInlineAdmin]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Debtor)