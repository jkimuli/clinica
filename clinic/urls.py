__author__ = 'julius'

from django.urls import path

from clinic import views
from .apps import ClinicConfig

app_name = ClinicConfig.name

urlpatterns = [

    path('', views.index, name='home'),

    path('patient', views.PatientListView.as_view(), name='patient_list'),
    path('employee', views.EmployeeListView.as_view(), name='employee_list'),
    path('visit', views.VisitListView.as_view(), name='visit_list'),

    path('patient/add', views.CreatePatientView.as_view(),name='patient_new'),
    path('employee/add', views.CreateEmployeeView.as_view(),name='employee_new'),
    path('visit/add', views.CreateVisitView.as_view(), name='visit_new'),

    #path patterns for editing model entities

    path('patient/edit/<int:pk>', views.UpdatePatientView.as_view(),name='patient_edit'),
    path('employee/edit/<int:pk>', views.UpdateEmployeeView.as_view(),name='employee_edit'),
    path('visit/edit/<int:pk>',views.UpdateVisitView.as_view(),name='visit_edit'),

    #path('patient/<int:pk>', views.DetailPatientView.as_view(),name='patient_detail'),
    path('employee/<int:pk>', views.DetailEmployeeView.as_view(),name='employee_detail'),
    path('visit/<int:pk>',views.DetailVisitView.as_view(),name='visit_detail'),

    path('patient/delete/<int:pk>', views.DeletePatientView.as_view(),name='patient_delete'),
    path('employee/delete/<int:pk>', views.DeleteEmployeeView.as_view(),name='employee_delete'),
    path('visit/delete/<int:pk>', views.DeleteVisitView.as_view(),name='visit_delete'),

    path('employee/<int:pk>/assigments',views.EmployeeAssignmentDetails.as_view(),name='employee_assignment'),
    path('employee/<int:pk>/expenses',views.EmployeeExpenseDetails.as_view(),name='employee_expense'),

    path('patient/<int:pk>/history',views.PatientHistoryView.as_view(),name='patient_history'),
    

]
