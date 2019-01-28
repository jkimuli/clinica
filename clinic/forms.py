from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from clinic.models import Employee,Patient


class EmployeeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ('username','email','phone','alternate_phone','designation',)

class EmployeeUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee  
        fields = ('username','email','phone','alternate_phone','designation',)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'gender': forms.Select()  
            
        }        