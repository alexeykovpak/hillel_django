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
from rest_framework.authtoken import views as rest_views
from core.views import GroupView, TeacherView, AddGroupView, AddStudentView, EditStudentView, EditGroupView, ContactUsView, ReturnCSV_View
from api import views as api_views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('csv/', ReturnCSV_View, name='return_csv'),
    path('groups/', GroupView.as_view(), name='group_list'),
    path('teachers/', TeacherView.as_view(), name='teacher_list'),
    path('add_group/', AddGroupView.as_view(), name='add_group'),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('edit_student/<int:pk>/', EditStudentView.as_view()),
    path('edit_group/<int:pk>/', EditGroupView.as_view()),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('contact_us/done/', TemplateView.as_view(template_name='contact_us_done.html'), name='contact_us_done'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/students/', api_views.StudentView.as_view({'get': 'list', 'post': 'create'})),
    path('api/students/<int:pk>/', api_views.StudentView.as_view({'put': 'update'})),
    path('api/groups/', api_views.GroupView.as_view({'get': 'list', 'post': 'create'})),
    path('api/groups/<int:pk>/', api_views.GroupView.as_view({'put': 'update'})),
    path('api/teachers/', api_views.TeacherView.as_view({'get': 'list', 'post': 'create'})),
    path('api/teachers/<int:pk>/', api_views.TeacherView.as_view({'put': 'update'})),
    path('api-token-auth/', rest_views.obtain_auth_token, name='api-tokn-auth')

]

