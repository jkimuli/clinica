# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView

from .models import LabTest, Item,Sale,SaleItem,SaleTest

from extra_views import InlineFormSetView,CreateWithInlinesView



class LabTestListView(ListView):
    model = LabTest
    context_object_name = "lab_tests"
    template_name = "sales/test_list.html"


class ItemListView(ListView):
    model = Item
    context_object_name = "drugs"
    template_name = "sales/item_list.html"


class ItemCreateView(CreateView):
    model = Item
    template_name = 'sales/item_add.html'


class LabTestCreateView(CreateView):
    model = LabTest
    template_name = 'sales/test_add.html'


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'sales/item_add.html'


class LabTestUpdateView(UpdateView):
    model = LabTest
    template_name = 'sales/add_lab_test.html'


class ItemDetailView(DetailView):

    pass


class LabTestDetailView(DetailView):
    pass


class ItemInline(InlineFormSetView):
    model = SaleItem


class TestInline(InlineFormSetView):
    model = SaleTest


class CreateSaleInline(CreateWithInlinesView):
    model = Sale
    inlines = [ItemInline,TestInline]
