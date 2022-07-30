from django.shortcuts import render, redirect

from .forms import *
from .models import *

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


from django.contrib.auth import login
from django.contrib import messages


from django.contrib.auth import login

class RegisterViewSet(ViewSet):

	def list(self, request):
		form = RegisterForm(None)
		return render(request=request, template_name="register.html", context={"register_form":form})

	def create(self, request):
		form = RegisterForm(request.data)
		if form.is_valid():
			teacher = form.save()
			return redirect("/register/")
		form = RegisterForm(None)
		return redirect("/register/")
		# return render(request=request, template_name="templates/register.html", context={"register_form":form})

class LoginViewSet(ViewSet):

	def list(self, request):
		form = LoginForm(None)
		return render(request=request, template_name="login.html", context={"login_form":form})

	def create(self, request):
		teacher = Teacher.objects.filter(phone=request.data['phone']).first()
		form = LoginForm(None)

		if teacher:
			if teacher.check_password(request.data['password']):
				login(request, teacher)
				return render(request=request, template_name="login.html", context={"login_form":form})
			else:
				return render(request=request, template_name="login.html", context={"login_form":form, "error": "Incorrect password"})
		else:
			return render(request=request, template_name="login.html", context={"login_form":form, "error": "No such phone"})
