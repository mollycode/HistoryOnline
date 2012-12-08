# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import NodeForm, Filter

def webdev(request):

	if request.method == 'POST':
		form = NodeForm(request.POST, request.FILES)
		if form.is_valid():
			new_node = form.save()
			new_filter = Filter(name=new_node.name, uid=new_node.id)
			new_filter.save()
			return HttpResponseRedirect('')

	else:
		form = NodeForm()

	return render_to_response('webdev.html',
		{'form':form},
		context_instance=RequestContext(request))