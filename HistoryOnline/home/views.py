# Create your views here.
from django.shortcuts import render_to_response
from HistoryOnline.webdev.models import Map

def home_screen(request):
	maps = Map.objects.all()
	return render_to_response('home_screen.html', {'maps':maps})
