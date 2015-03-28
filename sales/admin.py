__author__ = 'julius'

from django.contrib import admin
from .models import Item, Order, OrderItem, Supplier, Debtor


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'unit_cost',)
    search_fields = ('name', 'type')
    #radio_fields = {'type':admin.HORIZONTAL}


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address', 'phone', 'alternate_phone', 'email',)


class OrderItemInlineAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1


class DebtorInlineAdmin(admin.TabularInline):
	model = Debtor
	max_num = 1
	verbose_name = 'Add Debtor if not full payment'


class OrderAdmin(admin.ModelAdmin):
	inlines = [OrderItemInlineAdmin,]
	date_hierarchy = 'order_date'
	list_display = ('order_date','processed_by','total','item_names',)

	def save_related(self,request,form,formsets,change):
		super(OrderAdmin,self).save_related(request,form,formsets,change)
		order = form.instance
		order.total = 0

		for item in Order.objects.get(pk=order.id).items.all():
			order.total += (item.quantity*item.item.unit_cost)

		order.save()

		


	    




admin.site.register(Item, ItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Debtor)