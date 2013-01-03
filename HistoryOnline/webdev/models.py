from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.
class Map(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Filter(models.Model):
	title = models.ForeignKey(Map,null=True)
	name = models.CharField(max_length=50)
	uid = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Url(models.Model):
	url = models.URLField();

	def __str__(self):
		return url

class Node(models.Model):
	name = models.CharField(max_length=50)
	title = models.ForeignKey(Map,null=True)
	pic = models.ImageField(upload_to='images/%Y/%m/%d')
	summary = models.CharField(max_length=5000)
	source1 = models.URLField()
	source2 = models.URLField()
	source3 = models.URLField()
	filters = models.ManyToManyField(Filter,null=True,blank=True)
	relnodes = models.ManyToManyField("self",null=True,blank=True)

	def get_highlighted_node(nodeId):
		return node_set.get(name = nodeId)

	def __str__(self):
		return self.name

class NodeForm(ModelForm):
	def __init__(self, title, *args, **kwargs):
		super(NodeForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "*Title:"
		self.fields['pic'].label = "*Related image:"
		self.fields['source1'].label = "Additional research links:"
		self.fields['source1'].required = False
		self.fields['source2'].required = False
		self.fields['source3'].required = False
		self.fields['summary'] = forms.CharField(widget=forms.Textarea(attrs={'rows':25, 'cols':42, }))
		self.fields['summary'].label = "*Summary or additional notes:"
		self.fields['filters'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Filter.objects.filter(title=title), required=False)
		self.fields['filters'].label = "Add tags:"
		self.fields['relnodes'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Node.objects.filter(title=title), required=False)
		self.fields['relnodes'].label = "Add related events:"
		self.fields['title'].required = False

	class Meta:
		model = Node

class FilterForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FilterForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Name:"
		self.fields['title'].required = False

	name = forms.CharField(required=True)
	uid = forms.CharField(required=False)

	class Meta:
		model = Filter

class MapForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(MapForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "New Map Name:"
	
	name = forms.CharField(required=True)

	class Meta:
		model = Map