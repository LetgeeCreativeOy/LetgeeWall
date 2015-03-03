from django.db import models
import django.contrib.auth

# Create your models here.
class Event (models.Model):
	name 		= models.CharField ( max_length = 32 )
	description	= models.CharField ( max_length = 256 )
	#creator 	= models.User
	private		= models.BooleanField ( default = False )

