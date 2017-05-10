from django.conf.urls import url
from . import views

#https://tutorial.djangogirls.org/ko/django_urls/
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), #http://127.0.0.1:8000/post/1/
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]