from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the company')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    

    class Meta:
        verbose_name_plural = "companies"

    