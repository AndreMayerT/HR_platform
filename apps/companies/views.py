from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Company

# Create your views here.
class CompanyCreate(CreateView):
    model = Company
    fields = ['name']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return HttpResponse('OK')
    
class CompanyEdit(UpdateView):
    model = Company
    fields = ['name']