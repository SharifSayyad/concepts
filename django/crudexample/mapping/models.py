from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=50)
    pin = models.IntegerField()

 #   ad1 = Address(id=101,city='Pune',pin=411048)

class Cust(models.Model):
    cname = models.CharField(max_length=50)
    cage = models.IntegerField()
    address = models.OneToOneField(Address,related_name='user',on_delete=models.CASCADE,unique=True,null=True)

#c1 = Cust(id=1,cname='AAAA',cage='25')