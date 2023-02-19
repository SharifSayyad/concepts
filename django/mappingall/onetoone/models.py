from django.db import models
print('inside model')
# Create your models here.

class Emp(models.Model):
    myid = models.IntegerField(primary_key=True,default=0)
    name = models.CharField('emp_name', max_length=30)
    age = models.IntegerField('emp_age')
    salary = models.FloatField('emp_sal')
    #Emp(name='AAA',age=29,salary=5555)


class Address(models.Model):
    city = models.CharField('emp_city',max_length=30)
    state = models.CharField('emp_state',max_length=30)
    pin = models.IntegerField('emp_pincode')
    empref = models.OneToOneField('Emp',on_delete=models.CASCADE,
                                  null=True,unique=True)