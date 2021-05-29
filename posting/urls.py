from django.urls import path
from .views import PostList, PostDetail, postCreate

urlpatterns = [
	path("", PostList.as_view(), name="postList"),
	path("<int:pk>", PostDetail.as_view(), name="postDetail"),
	path("create", postCreate, name="postCreate"),
]