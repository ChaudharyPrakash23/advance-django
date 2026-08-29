from django.shortcuts import render
from .models import YouTubeUser
from django.core.cache import cache
# Create your views here.
def users_list(request):
    users=cache.get('users_data') #try to get data from cache
    if not users:
        print('cahce miss:Fetching data from database');
        users=YouTubeUser.objects.all()
        cache.set('users_data',users,timeout=600)
    else:
        print('cache hit:fetching data from cache')
        
    return render (request,'users_list.html',{'users':users})