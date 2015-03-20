__author__ = 'julius'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from clinic import views

urlpatterns = patterns(' ',
    url(r'^$', views.index, name='home'),

    url(r'^patient/$', views.PatientListView.as_view(), name='patient_list'),
    url(r'^employee/$', views.EmployeeListView.as_view(), name='employee_list'),
    url(r'^visit/$', views.VisitListView.as_view(), name='visit_list'),

    url(r'^patient/add/$', login_required(views.CreatePatientView.as_view()),name='patient_new'),
    url(r'^employee/add/$', login_required(views.CreateEmployeeView.as_view()),name='employee_new'),
    url(r'^visit/add/$', login_required(views.CreateVisitView.as_view()), name='visit_new'),


    #Url patterns for editing model entities

    url(r'^patient/edit/(?P<pk>\d+)/$', login_required(views.UpdatePatientView.as_view()),name='patient_edit'),
    url(r'^employee/edit/(?P<pk>\d+)/$', login_required(views.UpdateEmployeeView.as_view()),name='employee_edit'),
    url(r'^visit/edit/(?P<pk>\d+)/$',login_required(views.UpdateVisitView.as_view()),name='visit_edit'),


    url(r'^patient/(?P<pk>\d+)/$', views.DetailPatientView.as_view(),name='patient_detail'),
    url(r'^employee/(?P<pk>\d+)/$', views.DetailEmployeeView.as_view(),name='employee_detail'),
    url(r'^visit/(?P<pk>\d+)/$',views.DetailVisitView.as_view(),name='visit_detail'),

    url(r'^patient/delete/(?P<pk>\d+)/$', login_required(views.DeletePatientView.as_view()),name='patient_delete'),
    url(r'^employee/delete/(?P<pk>\d+)/$', login_required(views.DeleteEmployeeView.as_view()),name='employee_delete'),
    url(r'^visit/delete/(?P<pk>\d+)/$', login_required(views.DeleteVisitView.as_view()),name='visit_delete'),



)
