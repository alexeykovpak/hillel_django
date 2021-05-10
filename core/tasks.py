from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
import time
import core.models
from hillel_django.celery import app
from rest_framework.authtoken.models import Token

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

@app.task
def generate_new_token():
    for user in User.objects.all():
        Token.objects.create(user=user)
    # http POST http://127.0.0.1:8000/api-token-auth/ username='admin' password=''
    # f'http http://localhost:8081/api/user/ "Authorization: Token {API_KEY_HERE}"'

