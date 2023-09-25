from django.urls import path
from .views import DepartmentsList, DepartmentsCreate, DepartmentsUpdate, DepartmentsDelete

urlpatterns = [
    path('', DepartmentsList.as_view(), name='departments_list'),
    path('create/', DepartmentsCreate.as_view(), name='departments_create'),
    path('update/<int:pk>', DepartmentsUpdate.as_view(), name='departments_update'),
    path('delete/<int:pk>', DepartmentsDelete.as_view(), name='departments_delete')
]
