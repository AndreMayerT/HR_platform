from django.urls import path
from .views import EmployeeList, EmployeeEdit, \
 EmployeeDelete, EmployeeCreate

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee_list'),
    path('create/', EmployeeCreate.as_view(), name='employee_create'),
    path('edit/<int:pk>', EmployeeEdit.as_view(), name='employee_update'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='employee_delete')
]