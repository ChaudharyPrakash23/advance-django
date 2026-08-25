from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    response=HttpResponse('Cookie set succesfully')
    response.set_cookie('username','Prakash Chaudhary',max_age=60*60*24) #cookie valid for 1 day
    response.set_cookie('course','Advance Django',max_age=60*60*24)
    return response

def get_cookie(request):
    username=request.COOKIES.get('username','Guest')
    course=request.COOKIES.get('course','No course selected')
    
    if 'username' in request.COOKIES:
        return HttpResponse(f'username :{username},course:{course}')
    else:
        return HttpResponse('No Cookies Found')
    
def delete_cookie(request):
    response=HttpResponse('Cookie deleted successfully')
    response.delete_cookie()