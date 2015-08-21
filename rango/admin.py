from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):		#Only necessary if we want a custom admin view in the admin site
	list_display = ('title','category','url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
# Register your models here.
