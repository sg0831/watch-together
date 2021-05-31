from django import forms 
from django.contrib.auth.models import User

class Sign_upForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class Sign_inForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']