__author__ = 'julius'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns(' ',

    url(r'item/$', views.ItemListView.as_view(), name='item_list'),
    url(r'^test/$', views.LabTestListView.as_view(), name='test_list'),

    url(r'^item/new/$', login_required(views.ItemCreateView.as_view()), name='item_new'),
    url(r'^test/new/$', login_required(views.LabTestCreateView.as_view()), name='test_new'),

    url(r'^item/edit/(?P<pk>\d+)/$', login_required(views.ItemUpdateView.as_view()),name='item_edit'),
    url(r'^test/edit/(?P<pk>\d+)/$', login_required(views.LabTestUpdateView.as_view()),name='test_edit'),

    url(r'item/(?P<pk>\d+)/$',views.ItemDetailView.as_view(),name='item_detail'),
    url(r'test/(?P<pk>\d+)/$',views.LabTestDetailView.as_view(),name='test_detail'),

    #url(r'^sale/$', views.SaleListView.as_view(),name='sale_list'),
    url(r'^sale/new/$', views.CreateSaleInline.as_view(), name='sale_new'),

)
