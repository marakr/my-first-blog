from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

admin = User.objects.get(username='admin')
me2 = User.objects.get(username='me')

def post_list(request):
	#posts = Post.objects.filter(author=me2)
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  #publish 된것만 나온다
	return render(request, 'blog/post_list.html', {'posts': posts})