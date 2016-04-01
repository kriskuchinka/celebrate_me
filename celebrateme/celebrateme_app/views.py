from django.shortcuts import render, redirect
from django.http import HttpResponse
from celebrateme_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
	try:
		user = User.objects.create_user(username, email, password)

		return HttpResponse("New user has been created. Thank you for signing up.")
	except:
		return HttpResponse("Sorry. We are unable to create that user. Please try a different user name.")


def create_memorial(request):
	
	return render(request, "create_memorial.html")

def login_action(request):
    username = request.POST.get('username')
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect("/create_memorial/")
        else:
            # Return a 'disabled account' error message
            ...
    else:
        return HttpResponse(str(user) + ' is already logged in.')
        ...

def login_page(request):
	return render(request, "login.html")


def logout_action(request):
	logout (request)
	return redirect("/create_memorial/")













