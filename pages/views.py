from django.shortcuts import render
from clinic.models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all()    
    context = {
        'employees': employees,        
    }

    return render(request,'pages/index.html', context)
