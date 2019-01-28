__author__ = 'julius'

from django.urls import path
from . import views
from .apps import SalesConfig

app_name = SalesConfig.name

urlpatterns = [

    path('suppliers', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/add', views.SupplierCreateView.as_view(), name='supplier_add'),
    path('supplier/edit/<int:pk>', views.SupplierUpdateView.as_view(), name='supplier_edit'),
    path('supplier/delete/<int:pk>', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier_detail'),

    path('products',views.ProductListView.as_view(),name='product_list'),
    path('product/add', views.ProductCreateView.as_view(), name='product_add'),
    path('product/edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),

    path('orders',views.OrderListView.as_view(),name='order_list'),
    #path('order/new', views.OrderCreateView.as_view(), name='order_new'),
    #path('order/edit/<int:pk>', views.OrderUpdateView.as_view(), name='order_edit'),
    #path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='order_delete'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),

    path('purchases', views.PurchaseListView.as_view(), name='purchase_list'),
    path('purchase/add', views.PurchaseCreateView.as_view(), name='purchase_add'),
    path('purchase/edit/<int:pk>', views.PurchaseUpdateView.as_view(), name='purchase_edit'),
    path('purchase/delete/<int:pk>', views.PurchaseDeleteView.as_view(), name='purchase_delete'),
    path('purchase/<int:pk>', views.PurchaseDetailView.as_view(), name='purchase_detail'),



]
