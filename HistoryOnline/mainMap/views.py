# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from HistoryOnline.webdev.models import Node, Filter, Map

def mainMap(request, title, fil):
	full_title = title
	new_title = title.replace('_',' ')
	new_fil = fil.replace('_',' ')
	map_title = get_object_or_404(Map, name=new_title)
	if new_fil =='all':
		names = Node.objects.filter(title= map_title)
	else:
		f = get_object_or_404(Filter, name=new_fil)
		names = f.node_set.filter(title=map_title)
	filters = Filter.objects.filter(title=map_title)
	maps = Map.objects.all()
	return render_to_response('mainmap.html', 
		{'names': names, 'filters': filters, 'title':full_title, 'maps':maps}, 
		context_instance = RequestContext(request))

def mapIntro(request):
	maps = Map.objects.all()
	return render_to_response('mapIntro.html', {'maps':maps,})