# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class College(models.Model):
    collid = models.AutoField(primary_key=True)
    collname = models.CharField(max_length=50)
    collmaster = models.CharField(max_length=20)
    collweb = models.CharField(max_length=511, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_college'


class Teacher(models.Model):
    teaid = models.IntegerField(primary_key=True)
    teaname = models.CharField(max_length=20)
    teatitle = models.CharField(max_length=10, blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.PROTECT, db_column='collid')

    class Meta:
        managed = False
        db_table = 'tb_teacher'


class Course(models.Model):
    couid = models.IntegerField(primary_key=True)
    couname = models.CharField(max_length=50)
    coucredit = models.IntegerField()
    teacher = models.ForeignKey(to=Teacher, on_delete=models.PROTECT, db_column='teaid')
    students = models.ManyToManyField(to='Student', through='Score')

    class Meta:
        managed = False
        db_table = 'tb_course'


class Score(models.Model):
    scid = models.AutoField(primary_key=True)
    student = models.ForeignKey(to='Student', on_delete=models.PROTECT, db_column='stuid')
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT, db_column='couid')
    scdate = models.DateTimeField(blank=True, null=True)
    scmark = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_score'
        unique_together = (('student', 'course'),)


class Student(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=20)
    stusex = models.BooleanField(default=True)
    stubirth = models.DateField()
    stuaddr = models.CharField(max_length=255, blank=True, null=True)
    college = models.ForeignKey(to=College, on_delete=models.PROTECT, db_column='collid')
    courses = models.ManyToManyField(to=Course, through=Score)

    class Meta:
        managed = False
        db_table = 'tb_student'


