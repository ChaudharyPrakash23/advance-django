from django.shortcuts import render
from .models import UserList
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse

# Per view Cache

# @cache_page(30)
# def users_list(request):
#     print('Fetching userlist from database')
#     users=UserList.objects.all()
#     return render (request,'blog/users.html',{'users':users})



# Template Fragement Cache

def users_list(request):
    users=UserList.objects.all()
    return render (request,'blog/users.html',{'users':users})


def clear_cache(request):
    cache.clear()
    return HttpResponse('All Cache Cleared')