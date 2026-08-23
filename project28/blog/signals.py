from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog

#Trigger before saving the blog

@receiver(pre_save,sender=Blog)
def before_blog_save(sender,instance,**kwargs):
    print(f'about to save blog[Pre-Save]:{instance.title}')
    
#Trigger after saving blog
@receiver(post_save,sender=Blog)
def after_blog_save(sender,instance,created,**kwargs):
    if created:
        print(f"new blog created [Post-Save]:{instance.title}")
    else:
        print(f"Blog updated[Post-Save]:{instance.title}")