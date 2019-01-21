__author__ = 'julius'

from django.urls import path
from . import views

urlpatterns = [

    path('suppliers', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/new', views.SupplierCreateView.as_view(), name='supplier_new'),
    path('supplier/edit/<int:pk>', views.SupplierUpdateView.as_view(), name='supplier_edit'),
    path('supplier/delete/<int:pk>', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier_detail'),

    path('products',views.ProductListView.as_view(),name='product_list'),
    path('product/new', views.ProductCreateView.as_view(), name='product_new'),
    path('product/edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),

    path('invoices',views.OrderListView.as_view(),name='order_list'),
    #path('order/new', views.OrderCreateView.as_view(), name='order_new'),
    #path('order/edit/<int:pk>', views.OrderUpdateView.as_view(), name='order_edit'),
    #path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='order_delete'),
    #path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),


]
