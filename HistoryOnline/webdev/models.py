from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.
class Filter(models.Model):
	name = models.CharField(max_length=30)
	uid = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Node(models.Model):
	name = models.CharField(max_length=50)
	pic = models.ImageField(upload_to='images/%Y/%m/%d')
	summary = models.CharField(max_length=1000)
	sources = models.URLField()
	filters = models.ManyToManyField(Filter)

	def __str__(self):
		return self.name

class NodeForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(NodeForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Subtopic Title"
		self.fields['pic'].label = "Upload a image file"
		self.fields['sources'].label = "Enter addition research links:"
		self.fields['sources'].required = False
		self.fields['summary'].label = "Add summary and additional notes here:"
		self.fields['summary'] = forms.CharField(widget=forms.Textarea)
		self.fields['filters'].label = "Add hashtags (ex: #history #event1)"
		self.fields['filters'].required = False
		self.fields['filters'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Filter.objects.all())

	class Meta:
		model = Node