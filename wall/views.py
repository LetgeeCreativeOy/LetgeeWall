from django.shortcuts import render
from wall.models import Event, Message
from wall.forms import MessageForm




# Create your views here.
def home ( request ):

	if request.method == 'POST':
		form = MessageForm ( request.POST )
		if form.is_valid():
			x = 'Yay'
			boo = Message ( event=Event.objects.get(url_name="lc15"), message=form.cleaned_data['message'], sender = form.cleaned_data['author'] )
			boo.save ()
		else:
			x = 'Sad'

	else:
		form = MessageForm ()
		x = 'ASDASDAS'

	context = {
		"form" : form,
		"asd" : x,
	}
	return render ( request, "wall/index.html", context )


def show_events ( request ):
	events = Event.objects.order_by ("id")
	
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