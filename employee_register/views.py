from django.shortcuts import render,redirect
from .forms import EmployeeForm, RegisterForm
from .models import Employee
import os
from django.conf import settings
from django.contrib import messages
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    registerForm = RegisterForm(request.POST or None)
    if request.method == "POST":
        if registerForm.is_valid():
            registerForm.is_staff = True
            registerForm.save()

    return render(request, "registration/register.html", {"form": registerForm})

def employee_list(request):
    print (settings.BASE_DIR)
    context = {'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(instance=employee)
        return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST or None, request.FILES or None)
        else:
            employee = Employee.objects.get(id=id)
            employee.image.delete()
            form = EmployeeForm(request.POST or None, request.FILES or None, instance = employee)

        if form.is_valid():
            form.save()
            if id == 0:
                messages.success(request, "Employee Record Added Successfully!")
            else:
                messages.info(request,"Employee Record Updated Successfully!")

        return redirect("/employee/list")


def employee_delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.error(request, 'Employee Record Deleted Successfully!')

    return redirect('/employee/list')
