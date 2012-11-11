# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import NodeForm

def webdev(request):

	if request.method == 'POST':
		form = NodeForm(request.POST, request.FILES)
		if form.is_valid():
			new_node = form.save()
			return HttpResponseRedirect('/submit/')

	else:
		form = NodeForm()

	return render_to_response('webdev.html',
		{'form':form},
		context_instance=RequestContext(request))

def submitted(request):
	return render_to_response('submitted.html')