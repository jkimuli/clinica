from .models import Visit,Employee,Patient
from django.contrib import admin


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','designation','phone','alternate_phone','email',)
	search_fields = ('designation','first_name','last_name')
	list_filter = ('designation',)


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