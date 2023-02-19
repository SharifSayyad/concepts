from django.db import models
from django.db.models.signals import *
from django.dispatch import receiver
# Create your models here.

class Emp(models.Model):
    name = models.CharField('emp_name', max_length=30)
    age = models.IntegerField('emp_age')
    email = models.EmailField('emp_email',null=True)
    #salary = models.FloatField('emp_sal')
    #Emp(name='AAA',age=29,salary=5555)


class Address(models.Model):
    city = models.CharField('emp_city',max_length=30)
    state = models.CharField('emp_state',max_length=30)
    #pin = models.IntegerField('emp_pincode')
    empref = models.OneToOneField(Emp,on_delete=models.CASCADE,
                                  related_name='adrref',null=True)


# @receiver(pre_init,sender=Emp)
# def send_email(sender,**kwargs):
#     print(f'send email code will be here{sender}')
#
# @receiver(post_save,sender=Emp)
# def send_email1(sender,instance,*args,**kwargs):
#     print(f'email will be send to {instance.email}')
#     print(f'another parms {sender}')

# @receiver(post_save,sender=Emp)
# def send_msg_customer(sender,instance,created,raw,using,update_fields):
#     print('inside post save')

@receiver(post_save,sender=Emp)
def save_user_profile1(sender,instance,created,raw,using,update_fields,**kwargs):
    print('inside post save invoked')

@receiver(pre_save,sender=Emp)
def save_user_profile2(sender,instance,raw,using,update_fields,**kwargs):
    print(f'Pre save invoked {sender}{instance}{raw}{using}{update_fields}')

@receiver(pre_delete,sender=Emp)
def save_user_profile3(sender,instance,using,**kwargs):
    print(f'Pre Delete invoked {sender}{instance}{using}')

@receiver(post_delete,sender=Emp)
def save_user_profile4(sender,instance,using,**kwargs):
    print(f'post delete invoked {sender}{instance}{using}')

@receiver(pre_init,sender=Emp)
def save_user_profile5(sender,*args,**kwargs):
    print(f'pre init invoked {sender}')

@receiver(post_init,sender=Emp)
def save_profile6(sender,instance,**kwargs):
    print(f'post init invloked{sender} {instance}')


@receiver(m2m_changed,sender=Emp)
def reciver_function(sender,instance,action,reverse,model,pk_set,using,**kwargs):
    print(f'many to many invoked {sender} {instance}')