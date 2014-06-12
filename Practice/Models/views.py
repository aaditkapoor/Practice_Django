from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request,id):
	if id == None: return HttpResponse('No input provided!')
	return HttpResponse('Your ID is %s' % str(id))