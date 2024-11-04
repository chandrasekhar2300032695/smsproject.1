from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randomexamplecall/',views.randomexamplecall,name='randomexamplecall'),
    path('randomexamplelogic/',views.randomexamplelogic,name='randomexamplelogic'),
    path('calculatorcall/',views.calculatorcall,name='calculatorcall'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('loginpagecall/',views.loginpagecall,name='loginpagecall'),
    path('registerpagecall/',views.registerpagecall,name='registerpagecall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('logout/',views.logout,name='logout'),
    path('addstudent/',views.addstudentpagecall,name='addstudentpagecall'),
    path('addstudentlogic/',views.add_student,name='addstudentlogic'),
    path('studentlist/',views.student_list,name='student_list'),
    path('chart/',views.upload_file,name='upload_file'),
    path('user-input/', views.user_input_view, name='user_input'),
    path('success/<int:pk>/', views.success_page, name='success_page'),
    path('contact-manager/', views.contact_manager_view, name='contact_manager'),
    path('delete-contact/<int:pk>/', views.delete_contact_view, name='delete_contact'),


]