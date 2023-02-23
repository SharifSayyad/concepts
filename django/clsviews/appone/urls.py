from django.urls import path,include
from appone.urls import *
from appone.views import *
urlpatterns = [
   # path('admin/', admin.site.urls),
    #path('emp/',include('appone.urls'))
    path('save/',add_update_emp),
    path('edit/<int:eid>',fetch_for_edit),
    path('delete/<int:eid>',delete_emp),
    path('create/', AddEmp.as_view(),name="emp-create"),
    path('<int:pk>/update/', UpdateEmp.as_view(),name="emp-update"),
    path('<int:pk>/delete/', DeleteEmp.as_view(),name="emp-delete"),
    path('allemps/', AllEmps.as_view(),name="emp-list")
]
