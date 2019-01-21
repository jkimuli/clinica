
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from clinic.forms import EmployeeUserCreationForm,EmployeeUserChangeForm
from .models import Visit,Employee,Patient


class EmployeeAdmin(UserAdmin):
    add_form = EmployeeUserCreationForm
    form = EmployeeUserChangeForm
    model = Employee
    list_display = ('first_name','last_name','designation','phone','alternate_phone','email',)
    search_fields = ('designation','first_name','last_name')
    list_filter = ('designation',)
    fieldsets = (
		 ('Employee Info', {
			 'fields' : ('first_name','last_name','designation','phone','alternate_phone','email')
		 }),

		 ('Permissions',{
             'fields': ('is_active','is_staff','is_superuser')
		 })
	 )	 


class PatientAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','address','gender','dob','age',)
	search_fields = ('gender','first_name','last_name','address','age')
	list_filter = ('gender',)


class VisitAdmin(admin.ModelAdmin):
	list_display = ('visit_date','patient_id','examination','diagnosis','lab_tests','prescriptions',)
	search_fields = ('patient_id','diagnosis')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Visit,VisitAdmin)
admin.site.register(Patient,PatientAdmin)