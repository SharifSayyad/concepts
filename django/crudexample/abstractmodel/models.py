from django.db import models

# Create your models here.

#abstractmodel
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    class Meta:
        abstract =True


class Student(Person):
    Fees = models.FloatField()
    class Meta:
        abstract =True


class Employee(Person):
    salary = models.FloatField()
    class Meta:
        abstract = True

#p1 = Person(name='Sharif',age=26,email='sharif@gmail.com')

#s1 = Student(Fees=40120.145,name='Sachin',age=25,email='sachin@gmail.com')

#e1 = Employee(salary=657541.54)