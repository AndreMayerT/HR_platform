from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name