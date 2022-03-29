from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Posts, Blog
from django.urls import reverse_lazy
from .forms import PostsForm

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		template = 'list.html'
		posts = Posts.objects.all()
		context = {
			'posts': posts,
		}
		return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


def add_posts(request):
	if request.user.is_authenticated:
		template = "add_posts.html"
		if request.method == "POST":
			form = PostsForm(request.POST)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
		else:
			context = {
				'posts_form': PostsForm(),
			}
			return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


def delete_posts(request, posts_id):
	if request.user.is_authenticated:
		posts = Posts.objects.get(id=int(posts_id))
		posts.delete()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


def update_posts(request, posts_id):
	if request.user.is_authenticated:
		template = "update_posts.html"
		posts = Posts.objects.get(id=int(posts_id))

		if request.method =="POST":
			form = PostsForm(request.POST, instance=posts)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
		else:
			context = {
				'posts_form':PostsForm(instance=posts),
			}
			return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

