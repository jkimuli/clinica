
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Employee,Patient,Visit

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee

class EmployeeChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    list_display = ('first_name','last_name','designation','phone','alternate_phone','email')
    search_fields = ('designation','first_name','last_name')
    list_filter = ('designation',)
    list_per_page = 30  
    list_display_links=('first_name','last_name')    

    fieldsets = UserAdmin.fieldsets + (
        ('Employee Information', {'fields': ('hire_date','designation','phone',
                                'alternate_phone','is_mvp','employee_photo')}),
    )

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

