from django.urls import path, include
from . import views
app_name='facultyapp'
urlpatterns=[
    path('facultyhomepage/',views.facultyhomepage,name='facultyhomepage'),
    path('blogpage/',views.blogpagecall,name='blogpage'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<int:pk>/delete/', views.delete_task,name='delete'),
    path('add_course/',views.add_course,name='add_course'),
    path('view_student_list/',views.view_student_list,name='view_student_list'),
    path('postmarks/',views.post_marks,name='postmarks'),
]