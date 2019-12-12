from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
import os
from django.conf import settings

# Create your views here.
def employee_list(request):
    print (settings.BASE_DIR)
    context = {'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request, id=0):
    print(request)
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

        return redirect("/employee/list")


def employee_delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect('/employee/list')
