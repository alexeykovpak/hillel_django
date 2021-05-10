from django.db import models
from django.db.models.aggregates import Count, Avg, Max, Min
import time
from core.tasks import send_contact_us_email

class GroupManager(models.Manager):
    
    def get_group_with_student_count(self):
        return self.get_queryset().annotate(stq=Count('student'), stavg=Avg('student__age'), stmax=Max('student__age'), stmin=Min('student__age'))


class Teacher(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    objects = GroupManager()


class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    message = models.TextField()
    

    def __str__(self):
        return f'{self.name}, {self.email}'

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        send_contact_us_email.delay(self.name, self.message, self.email)

class Log(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    start_time = models.FloatField()
    time = models.FloatField()

    def __str__(self):
        show_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time)))
        return f'{show_time}, {self.path}'

class CurrencyRateParseData(models.Model):
    name = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)

    def __str__(self):
        return self.name

