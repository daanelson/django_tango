from django import forms
from rango.models import Page, Category

#This form lets us input a new category in Rango
class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='Please enter the category name.')
	
	#Note that all model fields need to either be initialized and hidden, or else 
	#expliicitly excluded (like in PageForm below)
	views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
	slug = forms.CharField(widget=forms.HiddenInput, required=False)

	#inline class to provide more information on the form (metadata)
	class Meta:
		model = Category
		fields = ('name',)

#This form lets us input a new Page in Rango
class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text='Please enter the page name.')
	url = forms.URLField(max_length=200, help_text='Please enter the URL of the page.')
	views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

	class Meta:
		model = Page
		#We also are telling the form what fields to exclude from itself. 
		#In this case, we want to exclude the category field (our ForeignKey)
		#Can do this by including fields with the keyword 'fields' or by:
		exclude = ('category',)

	def clean(self):
		#overriding clean method to include http:// on submitted urls
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

		return cleaned_data