import django_filters
from django.db.models import Q

from common.models import Student


def dealed_stuid(stuid):
     return stuid.replace(' ', '')


class StudentFilter(django_filters.FilterSet):
    stuname = django_filters.CharFilter(lookup_expr='contains')


    class Meta:
        model = Student
        fields = ('stuname', 'stuid', 'college')