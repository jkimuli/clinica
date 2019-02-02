# Create your views here.

from django.views.generic import CreateView,DetailView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import Expense
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

class ExpenseCreateView(UserPassesTestMixin,CreateView):
    fields = ('particulars','amount','incurred_by')
    model = Expense
    template_name = 'expenditure/expense_add.html'
    success_url = reverse_lazy('expenditure:expense_list')

    def test_func(self):
        return self.request.user.is_superuser

class ExpenseDetailView(LoginRequiredMixin,DetailView):

    pass


class ExpenseUpdateView(UserPassesTestMixin,UpdateView):
    fields = '__all__'
    model = Expense
    template_name = 'expenditure/expense_add.html'
    success_url = reverse_lazy('expenditure:expense_list')

    def test_func(self):
        return self.request.user.is_superuser


class ExpenseDeleteView(UserPassesTestMixin,DeleteView):

    def test_func(self):
        return self.request.user.is_superuser

class ExpenseListView(LoginRequiredMixin,ListView):
    model = Expense
    context_object_name = "expenses"
    template_name = 'expenditure/expense_list.html'

