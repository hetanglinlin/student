from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from api.filters import StudentFilter
from api.serializers import CollegeDetailSerializer, CourseSimpleSerializer, CourseDetailSerializer, \
    StudentDetailSerializer
from common.models import College, Course, Student


class CollegeView(ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeDetailSerializer
    pagination_class = None


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    pagination_class = None

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.only('couid', 'couname',)
        return self.queryset.prefetch_related('students').select_related('teacher')

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSimpleSerializer
        return CourseDetailSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().prefetch_related('courses')\
                        .select_related('college')
    serializer_class = StudentDetailSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = StudentFilter
    ordering = ('stuid')