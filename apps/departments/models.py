from django.db import models
from django.urls import reverse
from apps.companies.models import Company

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('departments_list')
    
    def __str__(self) -> str:
        return self.name