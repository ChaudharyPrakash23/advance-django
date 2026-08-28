from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mass_mail
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_bulk_email(request):
    message1=('welcome user 1','Welcome to platform!','chaudharyprakash023pc@gmail.com',['prakash.191527@ncit.edu.np'])
    message2=('welcome user 2','Welcome to platform!','chaudharyprakash023pc@gmail.com',['prachaucoc3@gmail.com'])
    
    send_mass_mail((message1, message2), fail_silently=False)
    
    return HttpResponse('Bluk emails sent successfully !')

# Now sending the html with mail
    
def send_html_email(request):
    subject="Welcome to my blog"
    from_email='chaudharyprakash023pc@gmail.com'
    recipient_list=['prakash.191527@ncit.edu.np','prachaucoc3@gmail.com']
    
    html_content=render_to_string('welcome_email.html',{'username':"Prakash"})
    
    msg=EmailMultiAlternatives(subject,"Welcome to My platform",from_email,recipient_list)
    msg.attach_alternative(html_content,'text/html')
    # msg.attach_file(yourcontent.pdf)  for attaching pdf or other files
    msg.send()
    
    return HttpResponse('Bulk email sent successfully')

