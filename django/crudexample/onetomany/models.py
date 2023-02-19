from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=30)
    eage = models.IntegerField()


class Address(models.Model):
    city = models.CharField(max_length=30)
    pin = models.IntegerField()
    cust = models.ForeignKey(Employee,related_name='emp',on_delete=models.CASCADE)

#e1 = Employee(ename='AAAA',eage=25)

#ad1 = Address(city='Pune',pin=411048)