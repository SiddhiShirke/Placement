from django.urls import path
from django.contrib import admin
from .views import signup,signin,logout,user_log,studentDataView,home,studentSection,profile,company_del,notadmin,coordinatorSection


urlpatterns = [
    path('',home),
    path('signup', signup),
    path('signin',signin),
    path('logout',logout),
    path('user',user_log),
    path('studentDataForm',studentDataView),
    path('studentSection',studentSection),
    path('profile',profile),
    path('comp',company_del),
    path('notadmin',notadmin),
    path('coordinatorSection',coordinatorSection)


]