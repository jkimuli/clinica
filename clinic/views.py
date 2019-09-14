from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic.edit import CreateView

from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .models import Visit,Employee,Patient
from .forms import PatientForm,VisitForm

from expenditure.models import Expense


def visit_index(request):
    # get the latest 50 clinic visits recorded in the database

    visits = Visit.objects.order_by('-visit_date')[:50] 
    paginator = Paginator(visits,1)
    page = request.GET.get('page')
    paged_visits = paginator.get_page(page)   

    context = {
        'visits': paged_visits
    }

    return render(request,'clinic/visits.html',context)

def dashboard(request):
    #get currently logged in user
    user = request.user

    # return expense report for current user
    expenses = Expense.objects.filter(incurred_by=user)[:5]


    #return visits handled by currently login user
    context = {
        'visits' : user.visits_handled.all()[:10],
        'expenses': expenses
    }
    return render(request,'clinic/dashboard.html', context )

def patient_index(request):
    patients = Patient.objects.all()
    paginator = Paginator(patients,1)
    page = request.GET.get('page')
    paged_patients = paginator.get_page(page)

    context = {
        'patients': paged_patients
    }

    return render(request,'clinic/patients.html', context)
    

def employee_index(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees,1)
    page = request.GET.get('page')
    paged_employees = paginator.get_page(page)

    context = {
        'employees': paged_employees
    }

    return render(request,'clinic/employees.html',context)

def visit_detail(request,visit_id):
    # return a single clinic record with the passed in visit_id

    visit = get_object_or_404(Visit,pk=visit_id)

    return render(request,'clinic/visit.html', {'visit': visit })

def patient_detail(request,patient_id):
    # return a single patient recrd with given patient_id

    patient = get_object_or_404(Patient,pk=patient_id)

    return render(request,'clinic/patient.html', {'patient': patient })    

def employee_detail(request,employee_id):
    # return a single employee with given id
    
    employee = get_object_or_404(Employee,pk=employee_id)
    return render(request,'clinic/employee.html', {'employee': employee })   

def visit_add(request):
    VisitFormSet = inlineformset_factory(Patient, Visit, extra=1, can_delete=False,form=VisitForm)                                    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        formset = VisitFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            patient = form.save()
            visits = formset.save(commit=False)
            for visit in visits:
                visit.patient = patient
                #visit.attendant = request.user.get_full_name()
                visit.save()                   

            return redirect('visits')        
    else:
        form = PatientForm()
        formset = VisitFormSet()

    return render(request,'clinic/record_add.html',{'form': form, 'formset': formset})  

def patient_edit(request,id):
    patient = get_object_or_404(Patient,pk=id)
    form = PatientForm(request.POST or None, instance=patient)

    if form.is_valid():
        form.save()
        return redirect('patients')   

    return render(request, 'clinic/patient_add.html', {'form': form, 'title':'Update Patient'}) 

def visit_edit(request,id):
    VisitFormSet = inlineformset_factory(Patient,Visit, extra=1, can_delete=False,form=VisitForm
                                    )
    visit = get_object_or_404(Visit,pk=id)
    patient = get_object_or_404(Patient,pk=visit.patient_id) 

    form = PatientForm(request.POST or None, instance=patient)
    formset = VisitForm(request.POST or None, instance=visit)

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()           

        return redirect('visits')

    return render(request,'clinic/record_add.html',{'form': form, 'formset': formset})                                           

    
           

            








