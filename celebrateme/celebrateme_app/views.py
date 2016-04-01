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

def create_memorial_action(request):
	first_name = request.POST.get('first_name')
	middle_name = request.POST.get('middle_name')
	last_name = request.POST.get('last_name')
	url_slug = '{}_{}'.format(first_name, last_name)
	date_of_birth = request.POST.get('date_of_birth')
	date_of_death = request.POST.get('date_of_death')

	deceased = Deceased(user_id=request.user, first_name=first_name, middle_name=middle_name, last_name=last_name, url_slug=url_slug, dob=date_of_birth, dod=date_of_death)
	deceased.save()

	""" This is not real code do not try to run...

	image_name = request.POST.get("image_name")
	image_src = request.POST.get('image_src')

	image = Image(deceased_id=deseased, image_name=image_name, image_src=image_src)

	image.save()"""
	return redirect('/memorial/' + url_slug)

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













