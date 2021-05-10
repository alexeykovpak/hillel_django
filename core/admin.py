from django.contrib import admin
from .models import Group, Student, Teacher, Log, Message, CurrencyRateParseData

# Register your models here.

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Log)
admin.site.register(Message)
admin.site.register(CurrencyRateParseData)

