from django.db import models

class Activity(models.Model):
	client = models.CharField(max_length=255)
	activity = models.CharField(max_length=255)
	activity_type = models.CharField(max_length=255)
	user = models.CharField(max_length=255)
	age = models.IntegerField()
	GENDERS = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
	gender = models.CharField(max_length=1, choices=GENDERS)
	location = models.CharField(max_length=255)
