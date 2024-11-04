from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def studenthomepage(request):
    return render(request, 'studentapp/studenthomepage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')
