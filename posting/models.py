from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField( max_length = 80 )
	content = models.CharField( max_length = 1000 )
	created = models.DateTimeField( auto_now=True )
	updated = models.DateTimeField( auto_now_add=True )
	user = models.ForeignKey( User, on_delete=models.CASCADE )
	def __str__(self):
		return self.title

class Photo(models.Model):
	post = models.ForeignKey( Post, on_delete=models.CASCADE )
	image = models.ImageField( upload_to="media/", blank=True )