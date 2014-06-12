from django.db import models

class Box(models.Model):
	firstname = models.CharField(max_length=200)
	date = models.DateTimeField('Date published')


