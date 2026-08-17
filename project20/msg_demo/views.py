from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request,'this is a debug message')
    messages.info(request,'this is general information')
    
    return render(request,'message.html')