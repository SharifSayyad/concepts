from django.shortcuts import render
import io
import json
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serializer import studentSeralizer

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,req,*args,**kwargs):
        json_data = req.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = studentSeralizer(stud)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")

        stud = Student.objects.all()
        serializer = studentSeralizer(stud,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self,req,*args,**kwargs):
        json_data = req.body
        # stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        pythondata = json.loads(json_data)
        serializer = studentSeralizer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"data Inserted"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def put(self,req,*args,**kwargs):
        json_data = req.body
        pythondata = json.loads(json_data)
        id = pythondata.get('id')
        try:
            stud = Student.objects.get(id=id)
        except Student.DoesNotExist:
            res = {"msg":"User Not Found"}
            return HttpResponse(json.dumps(res),content_type="application/json")
        serializer = studentSeralizer(stud,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = msg = {"msg":"Data Updated Sucess"}
            json_data = json.dumps(res)
            return HttpResponse(json_data,content_type="application/json")

        # json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json.dumps(serializer.errors), content_type="application/json")

    def delete(self,req,*args,**kwargs):
        json_data = req.body
        pythondata = json.loads(json_data)
        id = pythondata.get('id')
        try:
            stud = Student.objects.get(id=id)
        except Student.DoesNotExist:
            res ={"msg":"User Not Found"}
            return HttpResponse(json.dumps(res),content_type="application/json")
        stud.delete()
        res = {"msg":"User Delated Sucessfully"}
        return HttpResponse(json.dumps(res),content_type="application/json")



