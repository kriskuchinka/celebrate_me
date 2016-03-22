from django.db import models
# Need to figure out proper adding of User class and properties, because it is referenced in the Foreign Key in Deceased

class User(models.Model):
	"""I don't know what to put here at this point, but need it to reference to a ForeignKey in Deceased."""
	pass

class Deceased(models.Model):
	"""Defines the attributes and data points associated with the person who the memorial site is being created for."""

	#---!!!!----> How do I refer to User if I'm not supposed to create a model for one? ----!!!!
	user_id = models.ForeignKey(User)
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	url_slug = models.SlugField(max_length=100)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	dod = models.DateField(auto_now=False, auto_now_add=False)


class Image(models.Model):
	"""Stores and manages the images that users will upload to the site and share."""

	deceased_id = models.ForeignKey(Deceased)
	caption = models.CharField(max_length=250)
	source = models.ImageField(upload_to='deceased_pics')

class Biography(models.Model):
	"""Stores and manages the personal biography about the deceased person. Account user has full editing powers."""

	deceased_id = models.ForeignKey(Deceased)
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=600)
	survived_by = models.CharField(max_length=600)

class Quote(models.Model):
	"""Enables user to share a quote or saying and reference who said or wrote it. Ideally, something meaningful to the departed or their loved ones."""

	deceased_id = models.ForeignKey(Deceased)
	content = models.CharField(max_length=400)
	author = models.CharField(max_length=200)