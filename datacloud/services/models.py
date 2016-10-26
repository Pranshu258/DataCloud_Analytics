from django.db import models
from django.utils import timezone

class Activity(models.Model):
	timestamp = models.DateTimeField(default=timezone.now) 
	client = models.CharField(max_length=255)
	activity = models.CharField(max_length=255)
	activity_type = models.CharField(max_length=255)
	user = models.CharField(max_length=255)
	age = models.IntegerField()
	GENDERS = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
	gender = models.CharField(max_length=1, choices=GENDERS)
	location = models.CharField(max_length=255)

	def __str__(self):
		text = '\nClient: ' + self.client + '\n' + 'Activity: ' + self.activity + '\n' + 'Type: ' + self.activity_type + '\n' + 'Age: ' + str(self.age) + '\n' + 'Gender: ' + self.gender + '\n' + 'Timestamp: ' + str(self.timestamp) + '\n'
		return text