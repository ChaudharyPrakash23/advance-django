from django.shortcuts import render,redirect
from .forms import profileform
from .models import profile
from django.contrib import messages

# Create your views here.
def upload_profile(request):
    if request.method == 'POST':
        form=profileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'profile picture uploaded')
            return redirect('view_profile')
        else:
            messages.error(request,'unable to upload profile picture.Please try again!')
    else:
        form=profileform()
    return render(request,'accounts/upload_profile.html',{'form':form})
            
def view_profile(request):
    profiles=profile.objects.all()
    return render(request,'accounts/view_profile.html',{'profiles':profiles})
    