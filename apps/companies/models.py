from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the company')

    class Meta:
        verbose_name_plural = "companies"