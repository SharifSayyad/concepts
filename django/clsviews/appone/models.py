from django.db import models
from django.urls import reverse
# Create your models here.

class Employee(models.Model):
    name = models.CharField('emp_name',max_length=30)
    age = models.IntegerField('emp_age')
    salary = models.FloatField('emp_salary')
    role = models.CharField('emp_role',max_length=20)

    def get_absolute_url(self):
        return reverse('emp-list')

    @staticmethod
    def get_emp_instance():
        return Employee(id=0,name='',age='',salary='',role='')
    class Meta:
         db_table = 'emp_info'