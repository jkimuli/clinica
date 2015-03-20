__author__ = 'julius'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',


    url(r'^supplier/$', views.SupplierListView.as_view(), name='supplier_list'),
    url(r'^supplier/new/$', login_required(views.SupplierCreateView.as_view()), name='supplier_new'),
    url(r'^supplier/edit/(?P<pk>\d+)/$', login_required(views.SupplierUpdateView.as_view()), name='supplier_edit'),
    url(r'^supplier/delete/(?P<pk>\d+)/$', login_required(views.SupplierDeleteView.as_view()), name='supplier_delete'),
    url(r'^supplier/(?P<pk>\d+)/$', views.SupplierDetailView.as_view(), name='supplier_detail'),

)
