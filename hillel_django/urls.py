"""hillel_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from core.views import GroupView, TeacherView, AddGroupView, AddStudentView, EditStudentView, EditGroupView, ContactUsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('groups/', GroupView.as_view(), name='group_list'),
    path('teachers/', TeacherView.as_view(), name='teacher_list'),
    path('add_group/', AddGroupView.as_view(), name='add_group'),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('edit_student/<int:pk>/', EditStudentView.as_view()),
    path('edit_group/<int:pk>/', EditGroupView.as_view()),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('contact_us/done', TemplateView.as_view(template_name='contact_us_done.html'), name='contact_us_done'),
]

