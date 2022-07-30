from django.forms import ModelForm, CharField, PasswordInput, ModelMultipleChoiceField, Textarea
from .models import *

class RegisterForm(ModelForm):
	password = CharField(widget=PasswordInput)

	class Meta:
		model = Teacher
		fields = ['phone', 'first_name', 'last_name', 'subject', 'password']

	def save(self, commit=True):
		teacher = Teacher.objects.create(
			first_name=self.cleaned_data["first_name"],
			last_name=self.cleaned_data["last_name"],
			subject=self.cleaned_data["subject"],
			phone=self.cleaned_data["phone"],
		)

		teacher.set_password(self.cleaned_data["password"])
		teacher.save()

		return teacher


class LoginForm(ModelForm):
	password = CharField(widget=PasswordInput)

	class Meta:
		model = Teacher
		fields = ['phone', 'password']

class StudentCreateForm(ModelForm):

	def __init__(self, teacher, *args):
		super().__init__(*args)
		self.fields["clss"].queryset = Class.objects.filter(teacher=teacher)

	class Meta:
		model = Student
		fields = '__all__'

class StudentForm(ModelForm):

	class Meta:
		model = Student
		fields = '__all__'

class MessageForm(ModelForm):
	heading = CharField()
	content = CharField(widget=Textarea(attrs={"id": "message_content", "placeholder": "Message"}))
	classes = ModelMultipleChoiceField(queryset = Class.objects.all())

	def __init__(self, teacher, *args):
		super().__init__(*args)
		self.fields["classes"].queryset = Class.objects.filter(teacher=teacher)

	class Meta:
		model = School
		fields = ['heading', 'content', 'classes']