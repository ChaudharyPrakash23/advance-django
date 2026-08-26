from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
# def send_test_email(request):
#     subject='welcome to my blog'
#     message='thank you for subscribing my blog'
#     from_email='chaudharyprakash023pc@gmail.com'
#     recipient_list=['prakash.191527@ncit.edu.np']
#     send_mail(subject,message,from_email,recipient_list)
#     return HttpResponse('Test Mail sent successfully')

def send_test_email(request):
    subject='welcome to blog'
    message=render_to_string('email/email.html',{
                             'username':'Prakash',
                             'course':'Django-Tutoial'
                             })
    email=EmailMessage(
        subject,
        message,
        'chaudharyprakash023pc@gamil.com',
        ['prakash.191527@ncit.edu.np']
    )
    email.content_subtype='html'
    email.send()
    return HttpResponse ("email sent successfully")