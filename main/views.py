from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *

#Create your views here.
def home(request):
	form = DATA_FORM(request.POST,request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return HttpResponse('Form saved')
			
		else:
			return redirect("/")

	data = {
		'form':form
	} 
    
	return render(request,"home.html",data)