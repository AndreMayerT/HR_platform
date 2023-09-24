from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Employee
from django.views.generic import ListView, UpdateView, DeleteView

# Create your views here.

class EmployeeList(ListView):
    model = Employee
    
    def get_queryset(self) -> QuerySet[Any]:
        employee_company = self.request.user.employee.company

        return Employee.objects.filter(company=employee_company)
    
class EmployeeEdit(UpdateView):
    model = Employee
    fields = ['name', 'departments']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')