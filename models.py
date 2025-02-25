from django.db import models

# Create your models here.
class Survey_Data(models.Model):
    Initial_ID=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    Open_End=models.CharField(max_length=1000)
def __str__(self):
        return self.Initial_ID