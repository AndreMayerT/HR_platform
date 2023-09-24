from django.urls import path
from .views import EmployeeList, EmployeeEdit

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee_list'),
    path('edit/<int:pk>', EmployeeEdit.as_view(), name='employee_update')
]