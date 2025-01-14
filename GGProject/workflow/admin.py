from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Picture, Token
from .forms import EmployeeForm


# Defines admin view for Employee model
class EmployeeAdmin(UserAdmin):

    add_form = EmployeeForm
    model = Employee

    # Information shown about each Employee in list view
    list_display = ['username', 'first_name', 'last_name', 'emp_ID']
    # What attribute the Employees are sorted by in list view
    ordering = ('emp_ID',)

    # Fields available when adding a new Employee
    add_fieldsets = (
        ('User Information', {'fields': ('username', 'password1', 'password2')}),
        ('Personal Information', {'fields': ('first_name', 'last_name')}),
        ('Employee Information', {'fields': ('emp_ID', 'email', 'keycode', 'permissions')}),
        ('Account Information', {'fields': ('database_only', 'is_staff', 'is_superuser')}),
    )

    # Fields available when updating an Employee
    fieldsets = (
        ('User Information', {'fields': ('username', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name')}),
        ('Employee Information', {'fields': ('emp_ID', 'email', 'keycode', 'permissions')}),
        ('Account Information', {'fields': ('database_only', 'is_staff', 'is_superuser')}),
    )

    # Fields examined during search query
    search_fields = ('username', 'first_name', 'last_name', 'emp_ID')


# Unregister default models
admin.site.unregister(Group)
admin.site.unregister(Token)

# Register create models
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Picture)
