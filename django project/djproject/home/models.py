from django.db import models

# Create your models here.
class Enqry(models.Model):
    p_name= models.CharField(max_length=250)
    p_email=models.EmailField()
    p_phone=models.CharField(max_length=14)
    p_when=models.DateField()
    p_events=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.p_name} - {self.p_events} ({self.p_when})"