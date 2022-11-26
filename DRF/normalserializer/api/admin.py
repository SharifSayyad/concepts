from django.contrib import admin
from api.models import Student
# Register your models here.

# we can register your model in two way 1 @admin.register(Student) or
# admin.site.register(Student,StudentAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','city')
    # we can use tuple or list
    # list_display = ['id','name','roll','city']
admin.site.register(Student,StudentAdmin)