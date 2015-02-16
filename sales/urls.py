__author__ = 'julius'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',

    url(r'item/$', views.ItemListView.as_view(), name='item_list'),
    url(r'^test/$', views.LabTestListView.as_view(), name='test_list'),

    url(r'^item/new/$', login_required(views.ItemCreateView.as_view()), name='item_new'),
    url(r'^test/new/$', login_required(views.LabTestCreateView.as_view()), name='test_new'),

    url(r'^item/edit/(?P<pk>\d+)/$', login_required(views.ItemUpdateView.as_view()), name='item_edit'),
    url(r'^test/edit/(?P<pk>\d+)/$', login_required(views.LabTestUpdateView.as_view()), name='test_edit'),

    url(r'item/(?P<pk>\d+)/$', views.ItemDetailView.as_view(),name='item_detail'),
    url(r'test/(?P<pk>\d+)/$', views.LabTestDetailView.as_view(),name='test_detail'),

    #url(r'^sale/$', views.SaleListView.as_view(),name='sale_list'),
    url(r'^sale/new/$', views.CreateSaleInline.as_view(), name='sale_new'),

    #urls to deal with suppliers of drugs and lab regents

    url(r'^supplier/$', views.SupplierListView.as_view(), name='supplier_list'),
    url(r'^supplier/new/$', login_required(views.SupplierCreateView.as_view()), name='supplier_new'),
    url(r'^supplier/edit/(?P<pk>\d+)/$', login_required(views.SupplierUpdateView.as_view()), name='supplier_edit'),
    url(r'^supplier/delete/(?P<pk>\d+)/$', login_required(views.SupplierDeleteView.as_view()), name='supplier_delete'),
    url(r'^supplier/(?P<pk>\d+)/$', views.SupplierDetailView.as_view(), name='supplier_detail'),

)
