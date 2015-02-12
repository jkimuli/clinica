# Create your views here.

from django.views.generic import CreateView,DetailView,DeleteView,ListView,UpdateView
from .models import Expense

class ExpenseCreateView(CreateView):
    fields = ('particulars','amount','incurred_by')
    model = Expense
    template_name = 'expenditure/expense_add.html'

class ExpenseDetailView(DetailView):

    pass


class ExpenseUpdateView(UpdateView):

    pass


class ExpenseDeleteView(DeleteView):

    pass

class ExpenseListView(ListView):
    model = Expense
    context_object_name = "expenses"
    template_name = 'expenditure/expense_list.html'

