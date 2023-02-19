from django.shortcuts import render,redirect
from employee.models import Employee
from employee.forms import EmployeeForms

# Create your views here.

def emp(request):
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForms()
    return render(request,'index.html',{'form':form})
