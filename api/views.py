from django.views import View
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet, ModelViewSet
from api.serializers import StudentSerializer, GroupSerializer, TeacherSerializer
from api.serializers import UserSerializers
from core.models import Student, Group, Teacher


class Userviewsets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class StudentView(ViewSet):

    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse(StudentSerializer(obj).data, safe=False, status=201)
        return JsonResponse(serializer.errors)

    def update(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse(StudentSerializer(obj).data, safe=False, status=201)
        return JsonResponse(serializer.errors)

    def delete(self, request, pk):
        Student.objects.filter(id=pk).delete()
        return JsonResponse({'status': 'success'}, status=204)


class GroupView(ViewSet):

    def list(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse(GroupSerializer(obj).data, safe=False, status=201)
        return JsonResponse(serializer.errors)

    def update(self, request, pk):
        group = get_object_or_404(Group, id=pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse(GroupSerializer(obj).data, safe=False, status=201)
        return JsonResponse(serializer.errors)

    def delete(self, request, pk):
        Group.objects.filter(id=pk).delete()
        return JsonResponse({'status': 'success'}, status=204)


class TeacherView(ViewSet):

    def list(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse(TeacherSerializer(obj).data, safe=False, status=201)
        return JsonResponse(serializer.errors)

    def update(self, request, pk):
        teacher = get_object_or_404(Teacher, id=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse(TeacherSerializer(obj).data, safe=False, status=201)
        return JsonResponse(serializer.errors)

    def delete(self, request, pk):
        Teacher.objects.filter(id=pk).delete()
        return JsonResponse({'status': 'success'}, status=204)

