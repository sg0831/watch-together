from django.contrib import admin
from .models import Post, Photo, Comment

class PhotoInline( admin.TabularInline ):
	model = Photo
class PostAdmin( admin.ModelAdmin ):
	inlines = [ PhotoInline, ]

admin.site.register( Post, PostAdmin )
admin.site.register( Comment )