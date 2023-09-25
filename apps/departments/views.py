from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Department
from django.db.models.query import QuerySet
from typing import Any

# Create your views here.
class DepartmentsList(ListView):
    model = Department
    
    def get_queryset(self) -> QuerySet[Any]:
        company = self.request.user.employee.company

        return Department.objects.filter(company=company)
    
class DepartmentsCreate(CreateView):
    model = Department
    fields = ['name']

    def form_valid(self, form):
        department = form.save(commit=False)
        department.company = self.request.user.employee.company
        department.save()
        return super(DepartmentsCreate, self).form_valid(form)