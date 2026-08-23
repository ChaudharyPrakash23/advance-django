from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=25)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title