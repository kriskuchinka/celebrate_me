from django.shortcuts import render
from django.http import HttpResponse
from celebrateme_app.models import *
from django.contrib.auth.models import User


# Create your views here.

def index(request):
	return render(request, "index.html")

def user_display(request, name):
	try:
		person = Deceased.objects.get(url_slug__iexact=name)
	except:
		return render (request, "404_error.html")

	return render(request, "design1.html", {"person":person})

def sign_up(request):
	return render(request, "sign_up.html")

def create_user(request):
	username = request.POST.get("username")
	email = request.POST.get("email")
	password = request.POST.get("password")

	user = User.objects.create_user(username, email, password)
	
	return HttpResponse("Create User was called. username = {}, email = {}, password = {}".format(username, email, password))

def create_memorial(request):
	return render(request, "create_memorial.html")
