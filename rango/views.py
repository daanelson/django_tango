from django.shortcuts import render, HttpResponse

'''def index(request):
	return HttpResponse('Oh hey, world. Wanna know what it\'s <a href="/rango/about">all about?</a>')
	This is the old index method
'''

def index(request):

	#Construct a python dictionary which we can then pass the template engine
	#Note that we're defining {{ boldmessage }}, which we also placed into index.html
	context_dict = {'boldmessage':'What a bold, apposite message.'}

	return render(request, 'rango/index.html', context_dict)

def about(request):
	return HttpResponse('This page should probably be about something. <a href="/rango"> Whoops.</a>')

# Create your views here.
