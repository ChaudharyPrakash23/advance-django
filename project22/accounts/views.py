from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .form import RegistrationForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,'Registration success  you can login')
            return redirect('dashboard')
        else:
            messages.error(request,'registration failed.please correct the error below')
    else:
         form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'Login Successful')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})       

def logout_view(request):
    logout(request)
    messages.success(request,'logout successful')
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request,'accounts/dashboard.html')