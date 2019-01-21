__author__ = 'julius'

from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
      path('',views.ExpenseListView.as_view(),name='expense_list'),
      path('<int:pk>',views.ExpenseDetailView.as_view(),name='expense_detail'),
      path('edit/<int:pk>',views.ExpenseUpdateView.as_view(),name='expense_edit'),
      path('delete/<int:pk>',views.ExpenseDeleteView.as_view(),name='expense_delete'),
      path('add',views.ExpenseCreateView.as_view(),name='expense_create'),

]