from django.db import models
import django.contrib.auth
from django.utils import timezone

# Create your models here.
class Event ( models.Model ):
	name 			= models.CharField 		( max_length = 32, blank = False )
	description		= models.CharField 		( max_length = 256, blank = False )
	url_name		= models.CharField		( max_length = 16, default = "", blank = False )

	#creator 		= models.User
	
	private			= models.BooleanField 	( default = False )
	published		= models.DateTimeField 	( default = timezone.now() )

	logo_url		= models.CharField 		( max_length = 256, default = "", blank = True )
	hashtag			= models.CharField		( max_length = 32, default = "", blank = False )

	facebook		= models.BooleanField 	( default = True )
	twitter			= models.BooleanField	( default = True )
	instagram		= models.BooleanField	( default = True )
	
	allow_images	= models.BooleanField 	( default = False )
	block_words		= models.BooleanField 	( default = False )
	word_list_url 	= models.CharField 		( max_length = 256, blank = True )

	def __str__ (self):
		return self.name

class Message ( models.Model ):
	event 	=	models.ForeignKey 	( Event, default = 0 )
	message = 	models.CharField 	( max_length = 140 )
	sender	=	models.CharField 	( max_length = 32 )


	THIS 		= 'THIS'
	FACEBOOK 	= 'FACEBOOK'
	TWITTER 	= 'TWITTER'
	INSTAGRAM 	= 'INSTAGRAM'

	SERVICES = (
		( THIS, 	 "THIS" 	),
		( FACEBOOK,  "FACEBOOK"	),
		( TWITTER, 	 "TWITTER" 	),
		( INSTAGRAM, "INSTAGRAM"),
	)

	service = models.CharField ( max_length = 16,  choices = SERVICES, default = THIS )

	def __str__ (self):
		event_name = self.event.name[0:16] + "..." if len(self.event.name) > 16 else self.event.name
		return self.sender + ": " + event_name
