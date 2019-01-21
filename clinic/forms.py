from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from clinic.models import Employee


class EmployeeUserCreationForm(UserCreationForm):
    class Meta():
        model = Employee
        fields = ('username','email','phone','alternate_phone','designation',)

class EmployeeUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee  
        fields = ('username','email','phone','alternate_phone','designation',)