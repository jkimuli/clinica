# Create your views here.

from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.views.generic import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from clinic.models import Patient, Employee, Visit


def index(request):

    return render(request,'clinic/index.html')

class PatientListView(LoginRequiredMixin,ListView):
    model = Patient
    context_object_name = "patients"
    template_name = 'clinic/patient_list.html'

class EmployeeListView(LoginRequiredMixin,ListView):
    model = Employee
    context_object_name = "employees"
    template_name = "clinic/employee_list.html"


class VisitListView(LoginRequiredMixin,ListView):
    model = Visit
    context_object_name = "visits"
    template_name = "clinic/visit_list.html"


class CreatePatientView(LoginRequiredMixin,CreateView):
    model = Patient
    template_name = 'clinic/patient_add.html'


class CreateEmployeeView(UserPassesTestMixin,CreateView):
    model = Employee
    template_name = 'clinic/employee_add.html'

    def test_func(self):
        return self.request.user.is_superuser


class CreateVisitView(LoginRequiredMixin,CreateView):
    model = Visit
    template_name = 'clinic/visit_add.html'


class UpdatePatientView(LoginRequiredMixin,UpdateView):
    model = Patient
    template_name = 'clinic/patient_add.html'


class UpdateEmployeeView(UserPassesTestMixin,UpdateView):
    model = Employee
    template_name = 'clinic/employee_add.html'

    def test_func(self):
        return self.request.user.is_superuser


class UpdateVisitView(LoginRequiredMixin,UpdateView):
    pass


class DetailEmployeeView(LoginRequiredMixin,DetailView):
    model = Employee


class DetailPatientView(LoginRequiredMixin,DetailView):
    model = Patient


class DetailVisitView(LoginRequiredMixin,DetailView):
    model = Visit


class DeletePatientView(LoginRequiredMixin,DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')


class DeleteEmployeeView(UserPassesTestMixin,DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_superuser


class DeleteVisitView(LoginRequiredMixin,DeleteView):
    model = Visit
    success_url = reverse_lazy('visit_list')






