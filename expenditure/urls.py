__author__ = 'julius'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_index,name='expenses'),
    path('add', views.expense_add,name='expense_add'),  
    path('edit/<int:id>', views.expense_edit,name='expense_edit'),

    path('<int:id>', views.expense_detail,name='expense'),

]