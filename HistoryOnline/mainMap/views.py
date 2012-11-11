# Create your views here.
from django.shortcuts import render_to_response
from HistoryOnline.webdev.models import Node

def mainMap(request):
	names = Node.objects.all()
	return render_to_response('mainmap.html', {'names': names})
