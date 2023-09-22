from django.db import models

# Create your models here.
class OvertimeRegistration(models.Model):
    reason = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.reason