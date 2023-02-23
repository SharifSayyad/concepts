from django.shortcuts import render
from appone.models import *
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
        empinstance = Emp.objects.filter(id=formdata.get('eid')).first()
        if empinstance:
            empinstance.name = formdata.get('ename')
            empinstance.age = formdata.get('eage')
            empinstance.salary =formdata.get('esal')
            empinstance.email = formdata.get('eemail')
            empinstance.adrref.city = formdata.get('city')
            empinstance.adrref.state = formdata.get('state')
            empinstance.adrref.pin = formdata.get('pin')
            empinstance.save()
            empinstance.adrref.save()
            msg = 'Employee Updated Successfully..!'
        else:
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
    empinstance = Emp.objects.filter(id=eid).first()
    return render(request, 'index.html', {"resp": '', "elist": Emp.objects.all(),
                                          "emp": empinstance})


def delete_emp(request,eid):
    msg = ''
    dbemp = Emp.objects.filter(id=eid).first()
    if dbemp:
        dbemp.delete()
        msg = 'Employee Deleted Successfully..!'
    return render(request, 'index.html', {"resp": msg, "elist": Emp.objects.all(),
                                              "emp": Emp(None)})

