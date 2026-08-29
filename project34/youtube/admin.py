from django.contrib import admin
from django.contrib import messages
from django.core.cache import cache

from .models import YouTubeUser


@admin.action(description='Clear user Cache')
def clear_users_cache(modeladmin, request, queryset):
    cache.delete('users_data')
    messages.success(request, 'Users Cache cleared successfully')


@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'Subscribers')
    actions = [clear_users_cache]
