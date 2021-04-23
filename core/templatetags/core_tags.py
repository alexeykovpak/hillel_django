from django import template
from random import choice
from core.models import Teacher

register = template.Library()

@register.filter
def word_quantity_in_string(string):
    return len(string.split())

@register.filter
def even_numbers_from_object(obj):
    result = [number for number in obj if number % 2 == 0]
    return result

@register.simple_tag
def five_random_teachers():
    teachers = Teacher.objects.all()
    names = []
    for _ in range(5):
        names.append(choice(teachers).name)
    return names
    

