__author__ = 'julius'

from django.urls import path
from . import views
from .apps import ExpenditureConfig

app_name = ExpenditureConfig.name

urlpatterns = [
      path('',views.ExpenseListView.as_view(),name='expense_list'),
      path('<int:pk>',views.ExpenseDetailView.as_view(),name='expense_detail'),
      path('edit/<int:pk>',views.ExpenseUpdateView.as_view(),name='expense_edit'),
      path('delete/<int:pk>',views.ExpenseDeleteView.as_view(),name='expense_delete'),
      path('add',views.ExpenseCreateView.as_view(),name='expense_add'),

]