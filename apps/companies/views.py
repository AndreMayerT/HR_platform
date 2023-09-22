from django.shortcuts import render
from django.views.generic import CreateView
from .models import Company

# Create your views here.
class CompanyCreate(CreateView):
    model = Company