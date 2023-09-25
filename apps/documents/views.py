from django.shortcuts import render
from django.views.generic import CreateView
from .models import Document

# Create your views here.
class DocumentCreate(CreateView):
    model = Document
    fields = ['description', 'file']