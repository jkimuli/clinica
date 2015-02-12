__author__ = 'julius'

from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns(' ',

      url(r'^$',views.ExpenseListView.as_view(),name='expense_list'),
      url(r'^(?P<pk>\d+)/$',views.ExpenseDetailView.as_view(),name='expense_detail'),

      url(r'^edit/(?P<pk>\d+)/$',login_required(views.ExpenseUpdateView.as_view()),name='expense_edit'),
      url(r'^delete/(?P<pk>\d+)/$',login_required(views.ExpenseDeleteView.as_view()),name='expense_delete'),

      url(r'^add/$',login_required(views.ExpenseCreateView.as_view()),name='expense_create'),



    )