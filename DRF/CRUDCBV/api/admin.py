from django.contrib import admin
from api.models import Student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','city')

admin.site.register(Student,studentAdmin)
