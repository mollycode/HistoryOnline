from django import template
from django.template.defaultfilters import stringfilter
from HistoryOnline.webdev.models import Node

register = template.Library()

@register.filter(name='hovernode')
@stringfilter
def hovernode(value, id):
	n = Node.objects.get(name = 'n1')
	return n