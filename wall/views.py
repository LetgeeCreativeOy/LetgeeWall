from django.shortcuts import render
from wall.models import Event, Message



# Create your views here.
def home ( request ):
	return render ( request, "wall/index.html" )


def show_events ( request ):
	events = Event.objects.order_by ("+id")
	
	context = {
		"events" : events,
	}
	
	return render ( request, "wall/event_list.html", context )
	

def display_event ( request, event_url ):

	try:
		current_event = Event.objects.get (url_name=event_url)
	except Event.DoesNotExist:
		return render ( request, "404.html"  )


	try:
		messages = Message.objects.filter ( event = current_event ).order_by ("-id")
	except Message.DoesNotExist:
		messages = None



	context = {
		"event" : current_event,
		"messages" : messages,
	}

	return render ( request, "wall/event.html", context  )