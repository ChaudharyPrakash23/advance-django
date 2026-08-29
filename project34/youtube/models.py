from django.db import models

# Create your models here.
class YouTubeUser(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(unique=True)
    Subscribers=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name