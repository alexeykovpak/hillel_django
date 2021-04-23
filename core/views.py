from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls.base import reverse_lazy
from core.models import Group, Teacher, Student, Message
from core.forms import MyGroupForm, MyStudentModelForm
from .tasks import delete_old_logs

# Create your views here.

class GroupView(ListView):
    template_name = 'group_index.html'
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        groups = Group.objects.get_group_with_student_count().prefetch_related('teachers')
        context['groups'] = groups
        context['lst'] = [1, 2, 3, 4, 5, 6, 77, 88] #
        return context


class TeacherView(ListView):
    template_name = 'teacher_index.html'
    model = Teacher


class AddGroupView(TemplateView):
    template_name = 'add_group.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['form'] = MyGroupForm()
        return context

    def post(self, request):
        form = MyGroupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/groups/')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_responce(context)


class AddStudentView(CreateView):
    template_name = 'add_student.html'
    success_url = reverse_lazy('group_list')
    model = Student
    form_class = MyStudentModelForm


class EditGroupView(FormView):
    template_name = 'add_group.html'
    form_class = MyGroupForm
    success_url = reverse_lazy('group_list')

    def get_initial(self):
        name = Group.objects.get(id=self.kwargs['pk']).name
        return {'name': name}

    def form_valid(self, form):
        group = Group.objects.get(id=self.kwargs['pk'])
        group.name = form.cleaned_data['name']
        group.teachers.set(form.cleaned_data['teachers'])
        group.save()
        return super(EditGroupView, self).form_valid(form)


class EditStudentView(UpdateView):
    template_name = 'add_student.html'
    success_url = reverse_lazy('group_list')
    model = Student
    form_class = MyStudentModelForm

class ContactUsView(CreateView):
    template_name = 'contact_us.html'
    success_url = reverse_lazy('contact_us_done')
    model = Message
    fields = '__all__'

