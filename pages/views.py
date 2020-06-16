from django.shortcuts import render
from clinic.models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    mvp = Employee.objects.filter(is_mvp=True).first()
    context = {
        'employees': employees,
        'mvp' : mvp
    }

    return render(request,'pages/index.html',context)
