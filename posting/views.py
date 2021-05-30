from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Post, Photo

class PostList( ListView ):
	def get_queryset(self):
		return Post.objects.order_by("-created")[:5]

class PostDetail( DetailView ):
	model = Post

def postCreate(request):
	if request.method == 'POST':
		post = Post()
		post.title = request.POST['title']
		post.content = request.POST['content']
		post.created = timezone.datetime.now()
		post.user = request.user
		post.save()

		photo = Photo()
		photo.post = post
		for img in request.FILES.getlist('imgs'):
			photo.image = img
			photo.save()
		return redirect("/posts/" + str(post.id) )
	else:
		return render( request, "posting/post_create.html" )

def postUpdate( request, pk ):
	if request.method == 'POST':
		post = Post.objects.get( id=pk )
		post.title = request.POST['title']
		post.content = request.POST['content']
		post.updated = timezone.datetime.now()
		post.save()

		photo = Photo.objects.filter( post_id=pk )
		for img in request.FILES.getlist('imgs'):
			photo.image = img
			photo.save()
		return redirect("/posts/" )
	else:
		return render( request, "posting/post_update.html", {"post": Post.objects.get( id=pk ) })

def postDelete(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()

	return redirect("/posts")