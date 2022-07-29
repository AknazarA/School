from django.forms import ModelForm
from .models import Teacher

class RegisterForm(ModelForm):

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