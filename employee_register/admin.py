from django.contrib import admin
from .models import Employee, Position



@admin.register(Employee)
class EmployeeDetails(admin.ModelAdmin):
    list_display = ['fullname', 'mobile', 'emp_code', 'position', 'image']

admin.site.register(Position)