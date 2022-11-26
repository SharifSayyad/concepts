from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSeralizer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.
import json
# Model Object  - Single Data
def student_details(req,pk):
    msg = {"msg": "User Not Found"}
    try:
        stud = Student.objects.get(id=pk)
    except Exception:
        msg = {"msg": "User Not Found"}
    else:
        print(stud.__dict__)
        serializer = StudentSeralizer(stud)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    return HttpResponse(json.dumps(msg),content_type='application/json')

# get all student
def student_list(req):
    msg = {"msg": "User Not Found"}
    try:
        stud = Student.objects.all()
    except Exception:
        msg = {"msg": "User Not Found"}
    else:
        print(stud.__dict__)
        serializer = StudentSeralizer(stud,many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type='application/json')
        # if you want to use JsonResponse then
        # safe = False
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse(json.dumps(msg),content_type='application/json')