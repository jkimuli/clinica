# Create your views here.

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.views.generic import ListView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from clinic.models import Patient, Employee, Visit


def index(request):

    return render(request,'clinic/index.html')


class PatientListView(ListView):
    model = Patient
    context_object_name = "patients"
    template_name = 'clinic/patient_list.html'


class EmployeeListView(ListView):
    model = Employee
    context_object_name = "employees"
    template_name = "clinic/employee_list.html"


class VisitListView(ListView):
    model = Visit
    context_object_name = "visits"
    template_name = "clinic/visit_list.html"


class CreatePatientView(CreateView):
    model = Patient
    template_name = 'clinic/patient_add.html'


class CreateEmployeeView(CreateView):
    model = Employee
    template_name = 'clinic/employee_add.html'


class CreateVisitView(CreateView):
    model = Visit
    template_name = 'clinic/visit_add.html'


class UpdatePatientView(UpdateView):
    model = Patient
    template_name = 'clinic/patient_add.html'


class UpdateEmployeeView(UpdateView):
    model = Employee
    template_name = 'clinic/employee_add.html'


class UpdateVisitView(UpdateView):
    pass


class DetailEmployeeView(DetailView):
    model = Employee


class DetailPatientView(DetailView):
    model = Patient


class DetailVisitView(DetailView):
    model = Visit


class DeletePatientView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')


class DeleteEmployeeView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')


class DeleteVisitView(DeleteView):
    model = Visit
    success_url = reverse_lazy('visit_list')






