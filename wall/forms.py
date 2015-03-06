from django import forms

class MessageForm ( forms.Form ):
	author = forms.CharField ( max_length = 32 )
	message = forms.CharField ( max_length = 140 )
