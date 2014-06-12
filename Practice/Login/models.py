from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.username
class Passwords(models.Model):
	password =  models.CharField(max_length = 200)

	def __unicode__(self):
		return self.password