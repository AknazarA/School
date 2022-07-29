from django.db import models

class School(models.Model):
	name = models.CharField(max_length=255)

class Class(models.Model):
	name = models.CharField(max_length=255)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

class Teacher(models.Model):
	phone = models.CharField(max_length=15)
	clss = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
	subject = models.CharField(max_length=255)


def student_directory_path(instance, filename):
    return "student/{0}/{1}".format(instance.clss, filename)

class Student(models.Model):
	fio = models.CharField(max_length=255)
	email = models.EmailField()
	bdate = models.DateField()
	clss = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=1024)
	sex = models.CharField(max_length=6, choices= (('male', 'male'), ('female', 'female')))
	photo = models.ImageField(upload_to=student_directory_path, null=True, blank=True)
