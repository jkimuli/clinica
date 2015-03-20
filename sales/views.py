# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView

from .models import Item,Supplier,Debtor


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




