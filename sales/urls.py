__author__ = 'julius'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',


    url(r'^suppliers/$', views.SupplierListView.as_view(), name='supplier_list'),
    url(r'^supplier/new/$', login_required(views.SupplierCreateView.as_view()), name='supplier_new'),
    url(r'^supplier/edit/(?P<pk>\d+)/$', login_required(views.SupplierUpdateView.as_view()), name='supplier_edit'),
    url(r'^supplier/delete/(?P<pk>\d+)/$', login_required(views.SupplierDeleteView.as_view()), name='supplier_delete'),
    url(r'^supplier/(?P<pk>\d+)/$', views.SupplierDetailView.as_view(), name='supplier_detail'),

    url(r'^items/$',views.ItemListView.as_view(),name='item_list'),
    url(r'^item/new/$', login_required(views.ItemCreateView.as_view()), name='item_new'),
    url(r'^item/edit/(?P<pk>\d+)/$', login_required(views.ItemUpdateView.as_view()), name='item_edit'),
    url(r'^item/delete/(?P<pk>\d+)/$', login_required(views.ItemDeleteView.as_view()), name='item_delete'),
    url(r'^item/(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='item_detail'),

    url(r'^orders/$',views.OrderListView.as_view(),name='order_list'),
    #url(r'^order/new/$', login_required(views.OrderCreateView.as_view()), name='order_new'),
    #url(r'^order/edit/(?P<pk>\d+)/$', login_required(views.OrderUpdateView.as_view()), name='order_edit'),
    #url(r'^order/delete/(?P<pk>\d+)/$', login_required(views.OrderDeleteView.as_view()), name='order_delete'),
    #url(r'^order/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order_detail'),


)
