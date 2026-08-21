from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    category=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.title