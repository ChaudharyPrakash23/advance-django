from django.urls import path
from .import views

urlpatterns=[
    path('bulk-email/',views.send_bulk_email,name='send_bulk_email'),
    path('html-email/',views.send_html_email,name="send_html_email")
]