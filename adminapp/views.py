import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Task, StudentList
from .forms import TaskForm, StudentForm


# Create your views here.


def projecthomepage(request):
    return render(request, 'adminapp/projectHomePage.html')


def printpagecall(request):
    return render(request,'adminapp/printer.html')


def printpagelogic(request):
    if request.method=='POST':
        user_input=request.POST['user_input']
        print(f'User input: {user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)


def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')


def exceptionpagelogic(request):
    if request.method=='POST':
        user_input=request.POST['user_input']
        result=None
        error_msg=None
        try:
            num=int(user_input)
            result=10/num
        except Exception as e:
            error_msg=str(e)
        return render(request,'adminapp/ExceptionExample.html', {'result':result ,'error':error_msg})
    return render(request,'adminapp/ExceptionExample.html')


def randomexamplecall(request):
    return render(request,'adminapp/RandomExample.html')


def randomexamplelogic(request):
    if request.method=='POST':
        number1=int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=number1))
    a1={'ran':ran}
    return render(request,'adminapp/RandomExample.html',a1)


def calculatorcall(request):
    return render(request,'adminapp/calculator.html')


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form': form, 'tasks':tasks})


def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

def datetimepagecall(request):
    return render(request,'adminapp/datetimeexample.html')
import datetime
from datetime import timedelta


def datetimepagelogic(request):
    if request.method == 'POST':
        number1 = int(request.POST['date1'])
        x = datetime.datetime.now()
        print(x + datetime.timedelta(days=-81))
        ran=x + timedelta(days=number1)
    a1 = {'ran': ran}
    return render(request, 'adminapp/datetimeexample.html', a1)
def loginpagecall(request):
    return render(request,'adminapp/LoginPage.html')

def registerpagecall(request):
    return render(request, 'adminapp/Register.html')


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/projectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login



from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:studenthomepage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:facultyhomepage')  # Replace with your faculty homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/LoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/LoginPage.html')
    else:
        return render(request, 'adminapp/LoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'adminapp/addstudent.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/addstudent.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/addstudent.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})

def addstudentpagecall(request):
    return render(request,'adminapp/addstudent.html')


from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df=pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_Sales=df['Sales'].sum()
        average_Sales=df['Sales'].mean()

        df['Month']=df['Date'].dt.month
        monthly_Sales=df.groupby('Month')['Sales'].sum()
        month_names=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        monthly_Sales.index=monthly_Sales.index.map(lambda x: month_names[x-1])

        plt.pie(monthly_Sales, labels=monthly_Sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per month')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'adminapp/chart.html', {
            'total_Sales': total_Sales,
            'average_Sales': average_Sales,
            'chart': image_data
        })
    return render(request, 'adminapp/chart.html', {'form': UploadFileForm()})

from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import UserInput

def user_input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.save()
            return redirect('success_page', pk=user_input.pk)
    else:
        form = UserInputForm()
    return render(request, 'adminapp/user_input.html', {'form': form})

def success_page(request, pk):
    user_input = UserInput.objects.get(pk=pk)
    all_user_inputs = UserInput.objects.all()
    return render(request, 'adminapp/success.html', {'user_input': user_input, 'all_user_inputs': all_user_inputs})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact

def contact_manager_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_manager')
    else:
        form = ContactForm()
    contacts = Contact.objects.all()
    return render(request, 'adminapp/contact_manager.html', {'form': form, 'contacts': contacts})

def delete_contact_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_manager')