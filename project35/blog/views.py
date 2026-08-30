from django.shortcuts import render
from django.core.cache import cache

from .models import UserProfile


def user_profile_list(request):
    users_data = cache.get('users_data')

    if users_data is None:
        print('Fetching data from database')
        users_data = list(UserProfile.objects.all())
        cache.set('users_data', users_data, timeout=60)
    else:
        print('fetching data from cache')

    return render(request, 'users_profile_list.html', {'users': users_data})