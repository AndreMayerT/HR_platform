from django.db import models
from apps.employees.models import Employee

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Employee, on_delete=models.PROTECT)
    file = models.FileField(upload_to='documents')

    def __str__(self) -> str:
        return self.description