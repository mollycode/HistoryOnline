# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from HistoryOnline.webdev.models import Node, Filter, Map

def closeup(request, title, topic):
	new_topic = topic.replace('_',' ')
	node = get_object_or_404(Node, name=new_topic)
	reln = node.relnodes.all()
	fil = node.filters.all()
	maps = Map.objects.all()
	
	return render_to_response('closeup.html', 
		{'node': node,
		'reln': reln,
		'fil': fil,
		'maps': maps,
		'title': title}, 
		context_instance = RequestContext(request))
