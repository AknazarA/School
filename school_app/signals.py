from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from django.core.mail import send_mail


@receiver(post_save, sender=Student)
def send_email_to_student(sender, instance, **kwargs):
    send_mail(
        f'Welcome to our {instance.clss.school.name} school',
        f'Dear, {instance.fio}, you were added to {instance.clss.name} class.\nHappy learning!',
        'topeaky@gmail.com',
        [instance.email],
        fail_silently=False,
    )