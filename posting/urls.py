from django.urls import path
from .views import PostList, PostDetail, postCreate, postUpdate, postDelete, postLike, myTest, commentCreate

urlpatterns = [
	path("test/<int:pk>", myTest, name="myTest"),
	path("", PostList.as_view(), name="postList"),
	# crud
	path("create", postCreate, name="postCreate"),
	path("<int:pk>", PostDetail.as_view(), name="postDetail"),
	path("<int:pk>/update", postUpdate, name="postUpdate"),
	path("<int:pk>/delete", postDelete, name="postDelete"),
	# 좋아요
	path("<int:pk>/like", postLike, name="postLike"),
	# 댓글
	path("<int:post_id>/createComment", commentCreate, name="commentCreate"),
]