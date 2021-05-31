from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import Sign_upForm, Sign_inForm

def sign_up( request ):
	form_class = Sign_upForm
	# POST
	if request.method == "POST":
		form = Sign_upForm( request.POST )
		if form.is_valid():
			form.save()
			return redirect("/")

	# 회원가입 양식 전송
	else:
		form = Sign_inForm()
		return render( request, "account/sign_up.html", {'form': form} )


def sign_in( request ):
	form_class = Sign_inForm
	# POST
	if request.method == 'POST':
		form = Sign_inForm( request.POST )
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.get( username=username, password=password )

		if user != None:
			login(request, user)
			return redirect("/")
		else:
			return HttpResponse("로그인 실패: "+ username + ", " + password )

	# GET
	else:
		form = Sign_inForm()
		return render( request, "account/sign_in.html", {'form': form} )

def sign_out( request ):
	logout( request )
	return redirect("/")