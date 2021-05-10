from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Student, Group, Teacher


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.CharField()
    group = serializers.SlugRelatedField(many=False, read_only=False, slug_field='name', queryset=Group.objects.all())

    def create(self, validated_data):
        student, created = Student.objects.get_or_create(**validated_data)
        return student

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        teacher, created = Teacher.objects.get_or_create(**validated_data)
        return teacher

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class GroupSerializer(serializers.Serializer):
    name = serializers.CharField()
    teacher = serializers.SlugRelatedField(many=False, read_only=False, slug_field='name', queryset=Teacher.objects.all())

    def create(self, validated_data):
        group, created = Group.objects.get_or_create(**validated_data)
        group.save()
        return group

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

