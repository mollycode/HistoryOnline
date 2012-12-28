# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import NodeForm, Filter, FilterForm

def webdev(request):

	if request.method == 'POST':
		if 'node_sub' in request.POST:
			form = NodeForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('')
			else:
				nodeForm = form
				filterForm = FilterForm()
				
		elif 'filter_sub' in request.POST:
			form = FilterForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('')
			else:
				nodeForm = NodeForm()
				filterForm = form
	else:
		nodeForm = NodeForm()
		filterForm = FilterForm()

	return render_to_response('webdev.html',
		{'nodeForm':nodeForm,
		'filterForm':filterForm,},
		context_instance=RequestContext(request))