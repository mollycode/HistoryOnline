from django.db import models
from django.forms import ModelForm

# Create your models here.
class Node(models.Model):
	name = models.CharField(max_length=50)
	pic = models.ImageField(upload_to='images/%Y/%m/%d')
#	links = models.ManyToManyField('self')
	summary = models.CharField(max_length=400)
	
	def __str__(self):
		return self.name

class Filters(models.Model):
	name = models.CharField(max_length=30)
	nodes = models.ManyToManyField(Node)

	def __str__(self):
		return self.name

class NodeForm(ModelForm):
	class Meta:
		model = Node