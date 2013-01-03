# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import NodeForm, Filter, FilterForm, MapForm, Map, Node

def devlist(request):
	
	if request.method =='POST':
		form = MapForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		mapForm = MapForm()
		maps = Map.objects.all()
	
	return render_to_response('devlist.html', 
		{'mapForm':mapForm, 'maps':maps,}, 
		context_instance=RequestContext(request))

def webdev(request, title):
	new_title = title.replace('_',' ')
	new_map = get_object_or_404(Map, name=new_title)

	if request.method == 'POST':
		if 'node_sub' in request.POST:
			form = NodeForm(new_map, request.POST, request.FILES)
			if form.is_valid():
				new_node = form.save(commit=False)
				new_node.title = new_map
				new_node.save()
				form.save_m2m()
				return HttpResponseRedirect('')
			else:
				nodeForm = form
				filterForm = FilterForm()
				
		elif 'filter_sub' in request.POST:
			form = FilterForm(request.POST)
			if form.is_valid():
				fil = form.save(commit=False)
				fil.title = new_map
				fil.save()
				form.save_m2m()
				return HttpResponseRedirect('')
			else:
				nodeForm = NodeForm(new_map)
				filterForm = form
		elif 'review_sub' in request.POST:
			values = request.POST.getlist(u'deleted_nodes')
			for node in values:
				n = get_object_or_404(Node, name=node)
				n.delete()
			return HttpResponseRedirect('')
	else:
		nodeForm = NodeForm(new_map)
		filterForm = FilterForm()
		maps = Map.objects.all()
		nodes = Node.objects.filter(title=new_map)

	return render_to_response('webdev.html',
		{'nodeForm':nodeForm,
		'filterForm':filterForm,
		'new_map': new_map,
		'maps': maps,
		'nodes': nodes,},
		context_instance=RequestContext(request))