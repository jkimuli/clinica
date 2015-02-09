# Create your views here.

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.views.generic import ListView
from django.shortcuts import render

from clinic.models import Patient, Staff, Visit


def index(request):

    return render(request,'clinic/index.html')


class PatientListView(ListView):
    model = Patient
    context_object_name = "patients"
    template_name = 'clinic/patient_list.html'


class StaffListView(ListView):
    model = Staff
    context_object_name = "staff"
    template_name = "clinic/staff_list.html"


class VisitListView(ListView):
    model = Visit
    context_object_name = "visits"
    template_name = "clinic/visit_list.html"


class CreatePatientView(CreateView):
    model = Patient
    template_name = 'clinic/patient_add.html'


class CreateStaffView(CreateView):
    model = Staff
    template_name = 'clinic/staff_add.html'


class CreateVisitView(CreateView):
    model = Visit
    template_name = 'clinic/visit_add.html'


class UpdatePatientView(UpdateView):
    model = Patient
    template_name = 'clinic/patient_add.html'


class UpdateStaffView(UpdateView):
    model = Staff
    template_name = 'clinic/staff_add.html'


class UpdateVisitView(UpdateView):
    pass


class DetailStaffView(DetailView):
    model = Staff


class DetailPatientView(DetailView):
    pass

class DetailVisitView(DetailView):
    pass





