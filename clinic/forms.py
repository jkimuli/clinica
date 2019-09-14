from django.forms import ModelForm
from . models import Visit,Patient

class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['category','attendant','clinical_notes','lab_tests','prescriptions']  

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'