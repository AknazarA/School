from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('Teacher must have a phone')

        user = self.model(
            phone=phone,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        user = self.model(phone=phone)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


# _________________ Database Models _________________ #

class School(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Teacher(AbstractUser):
	phone = models.CharField(max_length=15, unique=True)
	subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)

	username = None
	email = None

	objects = MyUserManager()

	USERNAME_FIELD = "phone"
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = ("Teacher")
		verbose_name_plural = ("Teachers")


class Class(models.Model):
	name = models.CharField(max_length=255)
	teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	class Meta:
		verbose_name = ("Class")
		verbose_name_plural = ("Classes")

	def __str__(self):
		return self.name



def student_directory_path(instance, filename):
    return "student_images/{0}/{1}".format(instance.clss, f"{instance.fio}.jpg")

class Student(models.Model):
	fio = models.CharField(max_length=255)
	email = models.EmailField()
	bdate = models.DateField()
	clss = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=1024)
	sex = models.CharField(max_length=6, choices= (('male', 'male'), ('female', 'female')))
	photo = models.ImageField(upload_to=student_directory_path, null=True, blank=True)

	def __str__(self):
		return self.fio

	def get_name(self):
		fio = self.fio.split()
		return fio[1]
