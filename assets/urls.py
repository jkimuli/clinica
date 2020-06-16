__author__ = 'julius'

from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.asset_index,name='assets'),
    path('add', views.asset_add,name='asset_add'),
    path('edit/<int:id>', views.asset_edit, name='asset_edit')
        
]

