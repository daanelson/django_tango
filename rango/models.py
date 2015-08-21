from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)

	#Here we're overriding the default models.save function to generate slugs
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category,self).save(*args, **kwargs)

	def __unicode__(self): 	#my assumption is that we define fields & then this is a fxn that a model has to return its name
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title