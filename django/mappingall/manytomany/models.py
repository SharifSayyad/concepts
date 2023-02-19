from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField('emp_city', max_length=30)
    state = models.CharField('emp_state', max_length=30)
    pin = models.IntegerField('emp_pincode')

class Emp(models.Model):
    name = models.CharField('emp_name', max_length=30)
    age = models.IntegerField('emp_age')
    salary = models.FloatField('emp_sal')
    adrrefs = models.ManyToManyField(Address,
                                  related_name='emprefs')
