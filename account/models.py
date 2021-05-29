from django.db import models

class Account(models.Model):
	userName = models.CharField( max_length = 50 )
	password = models.CharField( max_length = 200 )
	email = models.CharField( max_length = 50 )
	phone = models.CharField( max_length = 20 )