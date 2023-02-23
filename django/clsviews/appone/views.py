from django.shortcuts import render
from .models import Employee
from django.urls import reverse_lazy

# Create your views here.
def add_update_emp(req):
    msg = ''
    if req.method == 'POST':
        fdata = req.POST
        eid = int(fdata.get('eid'))
        if eid > 0:
            dbemp = Employee.objects.filter(id=eid).first()
            dbemp.name = fdata.get('ename')
            dbemp.age = fdata.get('eage')
            dbemp.salary=fdata.get('esalary')
            dbemp.role=fdata.get('erole')
            dbemp.save()
            msg = 'Employee Updated Successfully..!!'
        else:
            e1 = Employee(name=fdata.get('ename'),age=fdata.get('eage'),
                     salary=fdata.get('esalary'),role=fdata.get('erole'))
            e1.save()
            msg = 'Employee Added Successfully..!!'
    return render(req, 'emp.html',{"resp": msg, "elist": Employee.objects.all(),
                               "emp": Employee.get_emp_instance()})

        #return render(request=req,template_name='emp.html',
                     # context={"resp":msg,"elist":Employee.objects.all(),
                      #         "emp":Employee.get_emp_instance()})



def fetch_for_edit(req,eid):
    dbemp = Employee.objects.filter(id=eid).first()
    return render(request=req, template_name='emp.html',
                  context={"resp": '', "elist": Employee.objects.all(),
                           "emp":dbemp})


def delete_emp(req,eid):
    msg = ''
    dbemp = Employee.objects.filter(id=eid).first()
    if dbemp:
        dbemp.delete()
        msg = 'Employee Deleted Successfully..!!'
    return render(request=req, template_name='emp.html',
                  context={"resp": msg, "elist": Employee.objects.all(),
                           "emp":Employee.get_emp_instance()})

from django.views.generic import CreateView,UpdateView,ListView,DeleteView

class AddEmp(CreateView):
    model = Employee # which model you want perfrom
    fields = '__all__'
    template_name = 'emp_create.html'
    msg = ''
    # fields = ('name','age') for specific field
    def get(self, request, *args, **kwargs):
        self.object = None
        AddEmp.msg = 'Get Method invoked'
        return super().get(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        AddEmp.msg = 'Post Method invoked'
        return super().post(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AddEmp, self).get_context_data(**kwargs)
        ctx['resp'] = AddEmp.msg
        return ctx


class DeleteEmp(DeleteView):
    model = Employee
    fields = '__all__'
    template_name = 'emp_delete.html'
    success_url = reverse_lazy('emp-list')


class AllEmps(ListView):
    model = Employee
    fields = '__all__'
    template_name = 'emp_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ''' for custom data'''
        ctx = super(AllEmps,self).get_context_data(**kwargs)
        ctx['emplist'] = Employee.objects.filter(id__gt=6).all()
        return ctx

class UpdateEmp(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'emp_update.html'


