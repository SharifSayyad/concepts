from django.shortcuts import render,HttpResponse
from endtoend.models import *


# Create your views here.
'''
in Flask
from flaks import request
@app.route('/index/',methods=["get","post"])
def welcome_page():
    if request.method =='post':
        formdata request.form  
    return render_template('index.html',named=value)

'''

def welcome_page(request):
    msg = ''
    if request.method=='POST':
        formdata = request.POST
        e1 = Emp(name=formdata.get('ename'),age=formdata.get('eage'),
                 salary=formdata.get('esal'),email=formdata.get('eemail'))
        adr1 = Address(city=formdata.get('city'),state=formdata.get('state'),
                       pin=formdata.get('pin'))
        e1.save()
        adr1.empref=e1
        adr1.save()
        msg = 'Employee added successfully.!'



    return render(request,'index.html',{"resp":msg,"elist":Emp.objects.all(),
                                        "emp":Emp(None)})


def edit_emp(request,eid):
    pass


def delete_emp(request,eid):
    pass

import json
from django.core.serializers import *

def emp_data_jsonview(request):

    emp_data = {'name':'sharif',
                'id':101,
                'salary':1554,
                'dept':'HR'}
    emp_data = Emp.objects.all()
    json_data = json.dumps(emp_data)

    return HttpResponse(json_data,content_type='application/json')

#using JsoneResponse
from django.http import JsonResponse
def emp_json_rsp(request):
    emp_data = {'name': 'sharif',
                'id': 101,
                'salary': 1554,
                'dept': 'HR'}
    emp_data = Emp.objects.all()
    print(emp_data)
    return JsonResponse(emp_data.__dict__)


def bd_data_emp(request):
    # emp_data = Emp.objects.all()
    emp_data = {'name': 'sharif',
                'id': 101,
                'salary': 1554,
                'dept': 'HR'}
    json_data = serialize('json',[emp_data,],fields=('name','id','salary'))

    return HttpResponse(json_data, content_type='application/json')

