from django import forms
from django.contrib.auth.models import User
from . models import Visit,Patient,Employee

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('category','clinical_notes','lab_tests','prescriptions') 

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']        

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')  

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('designation','phone','alternate_phone','employee_photo')