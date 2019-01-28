__author__ = 'julius'

from django.urls import path
from . import views
from .apps import AssetConfig

app_name = AssetConfig.name

urlpatterns = [
    
    path('',views.AssetListView.as_view(),name='asset_list'),
    path('<int:pk>',views.AssetDetailView.as_view(),name='asset_detail'),
    path('edit/<int:pk>',views.AssetUpdateView.as_view(),name='asset_edit'),
    path('delete/<int:pk>',views.AssetDeleteView.as_view(),name='asset_delete'),
    path('create',views.AssetCreateView.as_view(),name='asset_create'),
        
]

