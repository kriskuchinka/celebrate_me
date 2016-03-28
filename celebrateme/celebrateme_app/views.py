from django.shortcuts import render
from django.http import HttpResponse
from celebrateme_app.models import *


# Create your views here.

def index(request):
	return render(request, "index.html")

def design1(request):
	temp_var = Deceased.objects.all()
	person = temp_var[0]
	bio = Biography.objects.get(deceased_id=person.id)
	image = Image.objects.get(deceased_id=person.id)
	print(bio)
	return render(request, "design1.html", {"people":person, "bio":bio, "image":image})