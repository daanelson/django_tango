from django.shortcuts import render, HttpResponse
from rango.models import Category, Page 
from rango.forms import CategoryForm

'''def index(request):
	return HttpResponse('Oh hey, world. Wanna know what it\'s <a href="/rango/about">all about?</a>')
	This is the old index method
'''

def index(request):

	#Querydatabase for all categories currently stored
	# order by number of likes in descending order, retrieve top five
	# place list in context_dict which is then passed to template engine
	#Note that we're defining {{ boldmessage }}, which we also placed into index.html
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories':category_list}

	page_list = Page.objects.order_by('-views')[:5]
	context_dict['pages'] = page_list

	return render(request, 'rango/index.html', context_dict)

def about(request):
	return HttpResponse('This page should probably be about something. <a href="/rango"> Whoops.</a>')

# Creating a new view
def category(request, category_name_slug):
	context_dict = {}

	try:
		#goal is to see if a category with the given name slug already exists
		#if so, great, otherwise we raise some kind of exception
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		#retrieve all associated pages for given category
		#filter will return all objects which belong to the category we're looking at
		pages = Page.objects.filter(category=category)

		#sending our resultant pages to the template context under name "pages"
		context_dict['pages'] = pages

		#adding category object to context dict to prove that category is real
		context_dict['category'] = category

	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context_dict)
# Create your views here.

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		#check for valid form
		if form.is_valid():
			#save new category to database
			form.save(commit=True)

			#now call index view
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()

	return render(request, 'rango/add_category.html', {'form':form})
