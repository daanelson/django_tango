from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):		#Only necessary if we want a custom admin view in the admin site
	list_display = ('title','category','url')	#can use django documentation to learn much more about customizing this

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# Register your models here.
