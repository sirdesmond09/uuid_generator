from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    uuid = models.UUIDField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.uuid