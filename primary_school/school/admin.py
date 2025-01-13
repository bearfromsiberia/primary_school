from django.contrib import admin
from .models import Teacher, Class, Student, Parent, Homework, Grade

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialisation')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_id')
    list_filter = ('class_id',)
    search_fields = ('name',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'class_id')
    list_filter = ('teacher', 'class_id')
    search_fields = ('subject',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject', 'grade')
    list_filter = ('teacher', 'subject')
    search_fields = ('student__name', 'subject')
