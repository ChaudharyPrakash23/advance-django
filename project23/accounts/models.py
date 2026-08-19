from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='profiles/')
    
    def __str__(self):
        return self.name