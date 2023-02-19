from api.views import StudentAPI
from rest_framework.routers import DefaultRouter
routerobj = DefaultRouter()
routerobj.register('stud',StudentAPI)
urlpatterns = routerobj.urls