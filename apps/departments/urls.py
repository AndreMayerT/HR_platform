from django.urls import path
from .views import DepartmentsList

urlpatterns = [
    path('', DepartmentsList.as_view(), name='departments_list')
]
