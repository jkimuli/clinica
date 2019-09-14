__author__ = 'julius'

from django.urls import path
from clinic import views

urlpatterns = [

    path('visits', views.visit_index,name='visits'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('employees',views.employee_index,name='employees'),
    path('patients',views.patient_index,name='patients'),
    path('visit/<int:visit_id>',views.visit_detail,name='visit'),
    path('employee/<int:employee_id>',views.employee_detail,name='employee'),
    path('patient/<int:patient_id>',views.patient_detail,name='patient'),
    
    path('visits/add', views.visit_add, name='visit_add'), 
    path('patient/edit/<int:id>', views.patient_edit,name='patient_edit'), 

    path('visit/edit/<int:id>', views.visit_edit,name='visit_edit') 

]
