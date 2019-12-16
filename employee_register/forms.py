from django import forms
from .models import Employee
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee     
        fields = ('fullname', 'mobile', 'emp_code', 'position','image')
        labels = {
            'fullname': 'Full Name',
            'mobile': 'Mobile Number',
            'emp_code': "Employee Code",
            'position': "Position",
            'image': "Employee Image"
        }


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"
        self.fields['emp_code'].required = False
        # self.fields['image'].required = False

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =fields = ('email', 'username', 'password1', 'password2')
        