from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.description