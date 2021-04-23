from celery import shared_task
from hillel_django.celery import app
from django.conf import settings
from django.core.mail import send_mail
import time
import core.models

@app.task
def send_contact_us_email(name, message, email):
    send_mail(
    f'{name} sent a message for you',
    f'{message}\nemail: {email}',
    settings.SUPPORT_EMAIL_FROM,
    [settings.ADMIN_EMAIL],
    fail_silently=False,
    )

@app.task
def delete_old_logs():
    storage_time = time.time() - 604800
    old_logs = core.models.Log.objects.filter(start_time__lt=storage_time)
    old_logs.delete()

