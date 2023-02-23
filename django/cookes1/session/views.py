from django.shortcuts import render


def count_view(request):
    print('*****************************************************')
    formdata = request.GET
    sesval = formdata.get('name')
    val = request.session.get('name')
    print('hello')
    print(sesval)
    request.session['name'] = sesval
    return render(request,'count.html',{'name':val})

def delete_view(request):
    val = request.session.get('name')
    print('inside del')
    print(val)
    return render(request, 'delete.html',{'name':val})


def del_session(request):
    print('inside del_session')
    val = request.session.get('name')
    if val:
        del request.session['name']
        request.session.modified = True
        print('deleted')
    else:
        print('not deleted')
    return render(request, 'delete.html')
