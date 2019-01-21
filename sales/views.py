# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView

from .models import Product,Supplier,Order


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


class ProductListView(ListView):
    model = Product
    template_name = 'sales/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    pass


class ProductDeleteView(DeleteView):
    pass


class ProductCreateView(CreateView):
    model = Product
    template_name = 'sales/product_add.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'sales/product_add.html'


class OrderListView(ListView):
    model = Order
    template_name = 'sales/order_list.html'
    context_object_name = 'orders'






