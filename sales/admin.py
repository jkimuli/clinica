__author__ = 'julius'

from django.contrib import admin
from .models import Item, Order, OrderItem, Supplier, Debtor,Invoice,InvoiceItem


class InvoiceItemInlineAdmin(admin.TabularInline):
	model = InvoiceItem
	extra = 1

class InvoiceAdmin(admin.ModelAdmin):
	inlines = [InvoiceItemInlineAdmin,]

	fields = ('processed_by','payment_status','payment','customer')
	radio_fields = {'payment_status': admin.VERTICAL}
	list_display = ('invoice_date','processed_by','customer','total','payment_status','payment','item_names')

	def save_related(self,request,form,formsets,change):
		super(InvoiceAdmin,self).save_related(request,form,formsets,change)
		invoice = form.instance
		invoice.total = 0

		for item in Invoice.objects.get(pk=invoice.id).items.all():
			invoice.total += (item.quantity*item.item.unit_cost)

		invoice.save()

		# if payment status is not full paid or payment less than total - create Debtor object

		if invoice.payment_status =='P' or (invoice.payment < invoice.total):

			balance = invoice.total - invoice.payment

			p = Debtor.objects.create(customer=invoice.customer,bill=invoice.total,paid=invoice.payment,balance=balance,order=invoice)
			p.save()



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


class DebtorAdmin(admin.ModelAdmin):

	list_display = ('debt_date','customer','bill','paid','balance')

	def has_add_permission(self,request):
		return False


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
#admin.site.register(Order,OrderAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Debtor,DebtorAdmin)
admin.site.register(Invoice,InvoiceAdmin)