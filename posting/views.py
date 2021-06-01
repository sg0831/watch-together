from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from .models import Post, Photo, Comment, Friend

def myTest( request, pk ):
	post = Post( id=pk )
	text = "현재 접속 user :" + str( request.user.id ) + " post.like_users: " + str( post.like.all() )
	return render( request, "posting/test.html", {"text": text} )

class PostList( ListView ):
	def get_queryset(self):
		return Post.objects.order_by("-created")

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


def postLike( request, pk ):
	post = get_object_or_404( Post, id=pk )

	# 접속한 유저가 좋아요를 이미 눌렀으면
	if request.user in post.like.all():
		post.like.remove( request.user )
		post.like_count -= 1
		post.save()
	else:
		post.like.add( request.user )
		post.like_count += 1
		post.save()

	return redirect( "/posts/" + str(pk) )


def commentCreate( request, post_id ):
	# POST
	post = Post( id=post_id )
	if request.method == "POST":
		comment = Comment()
		comment.post = post
		comment.user = request.user
		comment.content = request.POST['content']
		comment.created = timezone.datetime.now()
		comment.updated = timezone.datetime.now()

		comment.save()
		return redirect( reverse( "postDetail", args=[comment.post.id] ) )


# 인기글
class PopularPost( ListView ):
	def get_queryset(self):
		return Post.objects.order_by("-like_count")

# 친구 리스트
class FriendList( ListView ):
	def get_queryset(self):
		return Friend.objects.all()