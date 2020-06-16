from django.urls import path
from . import views

urlpatterns = [
   path('suppliers', views.supplier_index,name='suppliers'),
   path('suppliers/add',views.supplier_add,name='supplier_add'),

   path('products', views.product_index,name='products'),
   path('products/add',views.product_add,name='product_add'),

   path('purchases', views.purchase_index,name='purchases'),
   path('purchases/add', views.purchase_add, name='purchase_add'),

   path('supplier/edit/<int:id>', views.supplier_edit,name='supplier_edit'),
   path('purchase/<int:id>', views.purchase_edit,name='purchase_edit'),
   path('product/<int:id>', views.product_edit,name='product_edit'),

   path('invoices', views.invoice_index,name='invoices'),
   path('invoices/add', views.invoice_add,name='invoice_add'),
   path('invoice/<int:id>',views.invoice_detail,name='invoice'),
   
]
