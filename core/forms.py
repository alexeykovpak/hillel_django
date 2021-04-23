from django import forms
from django.views.generic.base import TemplateView
from django.views.generic import FormView, CreateView
from core.models import Student, Teacher, Group


class MyGroupForm(forms.Form):
    name = forms.CharField(max_length=255)
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all())

    def save(self):
        teachers = self.cleaned_data.pop('teachers')
        group = Group.objects.create(
            **self.cleaned_data,
        )
        group.teachers.set(teachers)


class MyStudentModelForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ()
        widgets = {'group': forms.widgets.RadioSelect()}

