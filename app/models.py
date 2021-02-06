from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=220)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{str(self.name)}"