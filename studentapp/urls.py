from django.urls import path, include
from . import views
app_name='studentapp'
urlpatterns = [
    path('',views.studenthomepage,name='studenthomepage'),
   # path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('logout/',views.logout,name='logout'),

]