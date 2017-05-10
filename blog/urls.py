from django.conf.urls import url
from . import views

#https://tutorial.djangogirls.org/ko/django_urls/
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]