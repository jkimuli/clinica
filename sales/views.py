# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView
from django.urls import reverse_lazy

from .models import Product,Supplier,Order,Purchase


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
    fields = '__all__'
    template_name = 'sales/supplier_add.html'
    success_url = reverse_lazy('sales:supplier_list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'sales/supplier_add.html'
    fields='__all__'
    success_url = reverse_lazy('sales:supplier_list')


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
    fields = '__all__'
    success_url = reverse_lazy('sales:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'sales/product_add.html'
    fields = '__all__'
    success_url = reverse_lazy('sales:product_list')


class OrderListView(ListView):
    model = Order
    template_name = 'sales/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'sales/order_detail.html'
    context_object_name = 'order'


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'sales/purchase_list.html'
    context_object_name = 'purchases'


class PurchaseDetailView(DetailView):
    pass


class PurchaseDeleteView(DeleteView):
    pass


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'sales/purchase_add.html'
    fields = '__all__'
    success_url = reverse_lazy('sales:purchase_list')


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = 'sales/purchase_add.html'
    fields='__all__'
    success_url = reverse_lazy('sales:purchase_list')

class PaymentListView(ListView):
    template_name = 'sales/payment_list.html'
    queryset = Order.objects.filter(paid=False)
    context_object_name = 'orders'   







