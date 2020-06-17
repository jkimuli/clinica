from django.shortcuts import render
from clinic.models import Employee
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    #employees = Employee.objects.all()  
    users = User.objects.all().select_related('employee')  
    
    context = {
        'employees': users,        
    }

    return render(request,'pages/index.html', context)
