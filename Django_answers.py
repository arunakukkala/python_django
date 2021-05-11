1. What command line interface instructions are required to create a django project called
‘company’ and application called ‘staff’?

Answer: django-admin startproject company
            py manage.py startapp staff
            
            
2. models.py - Please use the django ORM framework to create the tables below.
Employee table
Employee name
Department
Email
Date of birth
Picture
Department table
Department name
Manager (employee)           

Answer:

from django.db import models

# Create your models here.
class Emplyoee(models.Model):
    Emplyoeename=models.CharField(max_length=30)
    Department=models.CharField(max_length=30)
    Email=models.EmailField()
    DateOfBirth=models.DateField()
    #picture=models.ImageField()

class Manager(models.Model):
    employee= models.CharField(max_length=50)
    def __str__(self):
        return self.employee

class Department(models.Model):
    DepartmentName=models.CharField(max_length=30)
    #manager = models.ForeignKey('employee')
    manager=models.ForeignKey('Manager',on_delete=models.CASCADE,)


3. admin.py - Please implement the code to allow the admin interface to be used to
manipulate the database for both the Employee and Department objects. When viewing
the Employee objects you should be able to filter by department and date of birth. When
creating/editing a Department object there should be inlines for each of the Employee
objects in the Department.

Answer:
from django.contrib import admin
from staff.models import Emplyoee,Department
# Register your models here.
class EmplyoeeAdmin(admin.ModelAdmin):
    list_display=['Emplyoeename','Department','Email','DateOfBirth']
admin.site.register(Emplyoee,EmplyoeeAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['DepartmentName','manager']
admin.site.register(Department,DepartmentAdmin)


4. What command line interface instructions are required to be able to test the admin interface after you have completed #2 and #3 above?

Answer:
py manage.py createsuperuser


5. views.py (Department) - Using generic class-based views please write the following views for the Department objects: list and detail

from django.views.generic.list import ListView
from .models import Department
class DeptList(ListView):
   model = Department
   
from django.views.generic.detail import DetailView
  
from .models import Department
  
class DeptDetailView(DetailView):
    
    model = Department

6. forms.py - Create a ModelForm class to create an Employee object only entering the Employee name and Department fields.
answer:
from django import forms
from staff.models import Emplyoee
class empform(forms.ModelForm):
    class Meta:
        model=Emplyoee
        #fields='__all__'
        fields={'Emplyoeename','Department'}


7.views.py (Employee) - Using a generic class-based view use the form in #6 in a create view for Employee objects. Is your models.py class for Employee compatible with the form and view?

8. What template files would be required for the views in #5 and #7 to work? Where would you put these files?

answer:

a)in question number 5 required two templates
path:COMPANY/templates/staff/template_name.html
b)in question number 7 required one template
path:staff/form_template_name.html



















