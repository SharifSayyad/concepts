from django.shortcuts import render

# Create your views here.

def count_view(request):
    count = int(request.COOKIES.get('count',0))
    newcount = count+1
    response =  render(request,'count.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=180)
    print('hello')
    print(request.headers.__dict__)
    return response

def delete_view(request):
    response = render(request, 'count.html')
    response.delete_cookie('count')
    return response