from django.conf.urls import patterns, url
#need to import url function so that we can call it below (urlpatterns does this)
from rango import views #importing our views.py from the app

#all urls that someone comes across have to be defined in urlpatterns, which is a tuple
urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^about',views.about,name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	)

