# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView

from .models import Item,Supplier,Debtor,Order


class SupplierListView(ListView):
    model = Supplier
    template_name = 'sales/supplier_list.html'
    context_object_name = 'suppliers'


class SupplierDetailView(DetailView):
    pass


class SupplierDeleteView(DeleteView):
    pass


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'sales/supplier_add.html'


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'sales/supplier_add.html'


class ItemListView(ListView):
    model = Item
    template_name = 'sales/item_list.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    pass


class ItemDeleteView(DeleteView):
    pass


class ItemCreateView(CreateView):
    model = Item
    template_name = 'sales/item_add.html'


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'sales/item_add.html'


class OrderListView(ListView):
    model = Order
    template_name = 'sales/order_list.html'
    context_object_name = 'orders'






