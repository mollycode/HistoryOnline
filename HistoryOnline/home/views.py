# Create your views here.
from django.shortcuts import render_to_response

def home_screen(request):
	return render_to_response('home_screen.html')
