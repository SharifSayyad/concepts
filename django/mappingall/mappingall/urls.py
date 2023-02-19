"""mappingall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from endtoend.views import *

from onetoone.views import *
from onetomany.views import *
print('inside urls.py')
urlpatterns = [
    path('admin/', admin.site.urls),

    path('emp/', welcome_page),
    path('emp/edit/<int:eid>', edit_emp),
    path('emp/delete/<int:eid>', delete_emp),
    path('welcome/',welcome),
    path('empjson/',emp_data_jsonview),
    path('dbemp/',bd_data_emp),
    path('empjsonrep/',emp_json_rsp)
]
