from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['username']='prakash'
    request.session['course']='Django full course'
    return HttpResponse("saved data successfully to session")

def get_session(request):
    username=request.session.get('username','guest')
    course=request.session.get('course','not enrolled')
    return HttpResponse (f'welcome:{username} ,you are learning:{course}')

def delete_session(request):
    request.session.flush()
    return HttpResponse("All data deleted successfully") 
#    or 
#    try:
#        del request.session.['username']
#        del reqeust.session.['course']
#    except KeyError:
#        pass
#    return HttpResponse("All data deleted successfully")   