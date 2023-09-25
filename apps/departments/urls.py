from django.urls import path
from .views import DepartmentsList, DepartmentsCreate

urlpatterns = [
    path('', DepartmentsList.as_view(), name='departments_list'),
    path('create/', DepartmentsCreate.as_view(), name='departments_create')
]
