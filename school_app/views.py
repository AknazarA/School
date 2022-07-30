from django.shortcuts import render, redirect

from .forms import *
from .models import *

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


from django.contrib.auth import login
from django.contrib import messages


from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterViewSet(ViewSet):

	template_register = "register.html"

	def list(self, request):
		form = RegisterForm(None)
		return render(request=request, template_name=self.template_register, context={"register_form": form})

	def create(self, request):
		form = RegisterForm(request.data)
		if form.is_valid():
			teacher = form.save()
			login(request, teacher)
			return redirect("/student/")
		form = RegisterForm(None)
		return redirect("/register/")

class LoginViewSet(ViewSet):

	template_login = "login.html"

	def list(self, request):
		form = LoginForm(None)
		return render(request=request, template_name=self.template_login, context={"login_form":form})

	def create(self, request):
		teacher = Teacher.objects.filter(phone=request.data['phone'])
		form = LoginForm(None)

		if teacher.exists() == False:
			return render(request=request, template_name=self.template_login, context={"login_form":form, "error": "No such phone"})

		teacher = teacher.first()
		if teacher.check_password(request.data['password']) == False:
			return render(request=request, template_name=self.template_login, context={"login_form":form, "error": "Incorrect password"})

		login(request, teacher)
		return redirect("/student/")

class StudentViewSet(LoginRequiredMixin, ViewSet):

    login_url = "/login/"
    template_student = "student.html"

    def list(self, request):
        if request.GET.get('name'):
            queryset = Student.objects.filter(clss__teacher=request.user, fio__contains=request.GET['name']).select_related('clss')
        else:
            queryset = Student.objects.filter(clss__teacher=request.user).select_related('clss')
        create_form = StudentForm(None)
        return render(request=request, template_name=self.template_student, context={"students": queryset, "create_form": create_form})


    def create(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/student/")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = Student.objects.get(id=pk)
        upadate_form = StudentForm(instance=student)
        return render(request=request, template_name="student_profile.html", context={"student": student, "upadate_form": upadate_form})

    def partial_update(self, request, pk=None):
        student = Student.objects.get(id=pk)
        form = StudentForm(request.data, instance=student)
        if form.is_valid():
            form.save()
            photo = request.data['photo']
            if photo:
                student.photo = photo
                student.save()
            return redirect(f'/student/{pk}/')
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Student.objects.get(id=pk).delete()
        return redirect("/student/")
