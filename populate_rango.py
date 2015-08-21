import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_django.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python',
        views = 128,
        likes = 64)
    print python_cat.views

    add_page(cat= python_cat,
        title='Official Python Tutorial',
        url='http://docs.python.org/2/tutorial/',
        views=23)

    add_page(cat=python_cat,
        title = 'thinking like a computer guy',
        url = 'http://www.greatneapress.com/thinkpython/',
        views=11)
    
    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=12)

    django_cat = add_cat('Django',
        views=64,
        likes=32)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=2)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=56)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=32)

    frame_cat = add_cat("Other Frameworks",
        views=32,
        likes=16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=33)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=34)


def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,likes,views):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.views=views
    c.save()
    return c

if __name__ == '__main__':
    print 'Starting Population script'
    populate()
