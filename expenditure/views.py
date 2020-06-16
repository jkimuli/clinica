# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .forms import ExpenseForm
from .models import Expense

# Create your views here.

def expense_index(request):
    expenses = Expense.objects.order_by('-expense_date')
    paginator = Paginator(expenses,1)
    page = request.GET.get('page')
    paged_expenses = paginator.get_page(page)   
    context = {
        'expenses': paged_expenses
    }

    return render(request,'expenditure/expenses.html', context)

def expense_add(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.incurred_by = request.user
            expense.save()
            return redirect(reverse('dashboard'))
    else:

        form = ExpenseForm()

    return render(request,'expenditure/expense_add.html',{'form': form , 'title': 'Add New Expense'})   

def expense_edit(request,id):
    expense = get_object_or_404(Expense,pk=id)
    form = ExpenseForm(request.POST or None, instance=expense)

    if form.is_valid():
        form.save()
        return redirect('expenses')

    return render(request,'expenditure/expense_add.html', {'form': form, 'title': 'Update Expense Record'})          

def expense_detail(request,id):
    expense = get_object_or_404(Expense,pk=id)
    return render(request,'expenditure/expense.html',{'expense': expense })    



        


