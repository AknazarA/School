from django.shortcuts import render, redirect

from .forms import *
from .models import *

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


from django.contrib.auth import login
from django.contrib import messages

class TeacherViewSet(ViewSet):

	def list(self, request):
		form = RegisterForm(None)
		print("Whaat")
		return render(request=request, template_name="register.html", context={"register_form":form})

	def create(self, request):
		form = RegisterForm(request.data)
		if form.is_valid():
			print("Success")
			teacher = form.save()
			return redirect("/register/")
		print("Wrong")
		form = RegisterForm(None)
		return redirect("/register/")
		# return render(request=request, template_name="templates/register.html", context={"register_form":form})