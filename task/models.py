from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=200)
	start = models.DateTimeField()
	end = models.DateTimeField()
	total = models.CharField(max_length=50)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title