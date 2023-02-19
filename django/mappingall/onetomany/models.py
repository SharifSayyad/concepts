from django.db import models

# Create your models here.

# table name will be onetomany_emp
class Emp(models.Model):
    name = models.CharField('emp_name', max_length=30)
    age = models.IntegerField('emp_age')
    salary = models.FloatField('emp_sal')
    email = models.EmailField('emp_email')


class Address(models.Model):
    city = models.CharField('emp_city', max_length=30)
    state = models.CharField('emp_state', max_length=30)
    pin = models.IntegerField('emp_pincode')
    empref = models.ForeignKey(Emp,related_name='adrrefs',on_delete=models.CASCADE,null=True)