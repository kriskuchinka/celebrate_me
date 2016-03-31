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
	return "Create User was called."
