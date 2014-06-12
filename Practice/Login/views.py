from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from Login.models import Users,Passwords


def start(request):
	return render_to_response('index.html',{},context_instance = RequestContext(request))

def register(request):
	user1 = Users(username = request.POST.get('username'))
	password1 = Passwords(password = request.POST.get('password'))
	
	user1.save()
	password1.save()

	return render_to_response('login.html',{'status': 'Registered'},context_instance = RequestContext(request))

def process(request):
	if Users.objects.filter(username__startswith=request.POST.get('username')) and Passwords.objects.filter(password__startswith=request.POST.get('password')):
		return HttpResponse('Hello, Logged!')
	else:
		return HttpResponse('Sorry! Incorrect<br>')

