
from django.contrib import admin
from .models import Employee,Patient,Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    
    list_display = ('user','designation','phone','alternate_phone','employee_photo','hire_date')
    search_fields = ('designation','user')
    list_filter = ('designation',)
    list_per_page = 30  
      

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','gender','age','address')
    search_fields = ('gender','first_name','last_name')
    list_filter = ('gender','address')
    list_per_page = 30

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('patient','visit_date','category','clinical_notes','attendant','lab_tests','prescriptions')
    search_fields = ('patient','category','attendant')
    list_filter = ('patient','visit_date','category','attendant')
    list_per_page = 30

