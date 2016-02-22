from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
# ^ -- "the beginning"
# post/ -- what comes next in the URL
# (?P<pk>[0-9]+) -- Django will take everything that is typed here and 
# define a variable pk (primary key). [0-9] also tells us that it can 
# only be an integer, not a letter (between 0 and 9). 
# + means that there needs to be one or more digits there.  
# So http://127.0.0.1:8000/post/1234567890/ but not /post//.
# $ -- "the end"

#Pages - A home page of post lists
#      - Pages for individual posts
#      - Page for make a new post
#      - Page to edit existing posts