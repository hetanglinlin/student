from rest_framework import serializers

from common.models import College, Course, Teacher, Student


class CollegeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'


class CourseSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('couid', 'couname')


class TeacherSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('teaid', 'teaname', 'teatitle')


class StudentSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('stuid', 'stuname')


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    @staticmethod
    def get_teacher(course):
        return TeacherSimpleSerializer(course.teacher).data

    @staticmethod
    def get_students(course):
        return StudentSimpleSerializer(course.students, many=True).data

    class Meta:
        model = Course
        fields = '__all__'


class CollegeSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = ('collid', 'collname')


class StudentDetailSerializer(serializers.ModelSerializer):
    college = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()

    @staticmethod
    def get_college(student):
        return CollegeSimpleSerializer(student.college).data

    @staticmethod
    def get_courses(student):
        return CourseSimpleSerializer(student.courses, many=True).data

    class Meta:
        model = Student
        fields = '__all__'