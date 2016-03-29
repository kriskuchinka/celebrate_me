from django.shortcuts import render
from django.http import HttpResponse
from celebrateme_app.models import *


# Create your views here.

def index(request):
	return render(request, "index.html")

def user_display(request, name):
	try:
		person = Deceased.objects.get(url_slug__iexact=name)
	except:
		return render (request, "404_error.html")

	bio = Biography.objects.get(deceased_id=person.id)
	image = Image.objects.get(deceased_id=person.id)
	quote = Quote.objects.get(deceased_id=person.id)
	print(bio)
	return render(request, "design1.html", {"person":person, "bio":bio, "image":image, "quote":quote})

	