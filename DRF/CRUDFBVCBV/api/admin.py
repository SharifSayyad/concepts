from django.contrib import admin
from api.models import Student
# Register your models here.
from django.contrib.admin.models import LogEntry

class studentAdmin(admin.ModelAdmin):
    list_display = ('name','roll','city')


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        print("user=",request.__dict__)
        print(change)
        obj.save()
        # user = LogEntry.objects.filter(request.user)
        # print(type(user))



admin.site.register(Student,studentAdmin)


