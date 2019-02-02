# Create your views here.

from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.views.generic import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from clinic.models import Patient, Employee, Visit
from clinic.forms import EmployeeUserCreationForm,EmployeeUserChangeForm,PatientForm


def index(request):

    return render(request,'clinic/index.html')

class PatientListView(LoginRequiredMixin,ListView):
    model = Patient
    context_object_name = "patients"
    template_name = 'clinic/patient_list.html'
    paginate_by=1

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
    form_class = PatientForm
    success_url = reverse_lazy('clinic:patient_list')


class CreateEmployeeView(UserPassesTestMixin,CreateView):
    model = Employee
    form_class= EmployeeUserCreationForm
    template_name = 'clinic/employee_add.html'
    success_url = reverse_lazy('clinic:visit_list')

    def test_func(self):
        return self.request.user.is_superuser


class CreateVisitView(LoginRequiredMixin,CreateView):
    model = Visit
    template_name = 'clinic/visit_add.html'
    fields = '__all__'
    success_url = reverse_lazy('clinic:visit_list')


class UpdatePatientView(LoginRequiredMixin,UpdateView):
    model = Patient
    template_name = 'clinic/patient_add.html'
    fields = '__all__'
    success_url = reverse_lazy('clinic:patient_list')


class UpdateEmployeeView(UserPassesTestMixin,UpdateView):
    model = Employee
    form_class=EmployeeUserChangeForm
    template_name = 'clinic/employee_add.html'

    def test_func(self):
        return self.request.user.is_superuser


class UpdateVisitView(LoginRequiredMixin,UpdateView):
    model = Visit
    fields = '__all__'
    template_name = 'clinic/visit_add.html'
    success_url = reverse_lazy('clinic:visit_list')


class DetailEmployeeView(LoginRequiredMixin,DetailView):
    model = Employee
    template_name = 'clinic/employee_detail.html'
    context_object_name = 'employee'


class PatientHistoryView(LoginRequiredMixin,DetailView):
    model = Patient
    template_name = 'clinic/patient_detail.html'
    context_object_name = 'patient'

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

class EmployeeAssignmentDetails(LoginRequiredMixin,DetailView):
    model = Employee
    template_name = 'clinic/employee_assignment.html'
    context_object_name = 'employee'

class EmployeeExpenseDetails(LoginRequiredMixin,DetailView):
    model = Employee
    template_name = 'clinic/employee_expense.html'
    context_object_name = 'employee'







