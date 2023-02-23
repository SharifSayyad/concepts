from django.shortcuts import render,HttpResponse
from .models import *
from django import forms
from .forms import *
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        phone = int(data['phone'])
        salary = int(data['salary'])
        bonus = int(data['bonus'])
        role = data['role']
        dept = data['dept']
        new_emp = Employee(first_name=first_name,last_name=last_name,phone=phone,salary=salary,
                           bonus=bonus,dept_id = dept,role_id = role,hire_date = datetime.now())
        new_emp.save()
        print('inside save')
        return HttpResponse('Employee Added Successfully..!')
    else:
        print('not')
        return render(request, 'add_emp.html')
    return render(request,'add_emp.html')

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')


def studentinputview(request):
    form = StudentForm()
    print('inside student view')
    if request.method =='POST':
        print('inside if')
        form = StudentForm(request.POST)
        if form.is_valid():
            print('success')

            print('Name:',form.cleaned_data['name'])
    return render(request,'student.html',{'form':form})