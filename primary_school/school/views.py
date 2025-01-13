from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Teacher, Class, Student, Parent, Homework, Grade

def index(request):
    return render(request, 'pages/home.html')


def class_list(request):
    template = 'pages/class_list.html'
    classes = Class.objects.all().order_by('name')
    context = {
        'classes': classes
    }
    return render(request, template, context)


def teacher_list(request):
    template = 'pages/teacher_list.html'
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, template, context)


# def get_students_list(teacher):
#     # Получить всех учеников, которых учит данный учитель через связанные классы
#     students = Student.objects.filter(class_id__homework__teacher=teacher).distinct()
#     return [student.name for student in students]
def get_students_list(teacher):
    if not isinstance(teacher, Teacher):
        raise ValueError("Ожидался объект Teacher, но получен другой тип.")

    # Получение студентов, связанных с учителем через домашние задания
    students = Student.objects.filter(
        class_id__homeworks__teacher=teacher
    ).distinct()

    return students

def teacher_dashboard(request, teacher_id):
    template = 'pages/teacher_dashboard.html'
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    homeworks = Homework.objects.filter(teacher=teacher)
    grades = Grade.objects.filter(teacher=teacher)
    students = get_students_list(teacher)

    context = {
        'teacher': teacher,
        'homeworks': homeworks,
        'grades': grades,
        'students': students,
    }
    return render(request, template, context)


def parent_dashboard(request, parent_id):
    template = 'pages/parent_dashboard.html'
    parent = get_object_or_404(Parent, pk=parent_id)
    students = parent.students.all()

    students_details = [
        {
            'name': student.name,
            'homeworks': Homework.objects.filter(class_id=student.class_id),
            'grades': Grade.objects.filter(student=student),
        }
        for student in students
    ]

    context = {
        'parent': parent,
        'students_details': students_details,
    }
    return render(request, template, context)


def student_dashboard(request, student_id):
    template = 'pages/student_dashboard.html'
    student = get_object_or_404(Student, pk=student_id)

    homeworks = Homework.objects.filter(class_id=student.class_id)
    grades = Grade.objects.filter(student=student)

    context = {
        'student': student,
        'homeworks': homeworks,
        'grades': grades,
    }
    return render(request, template, context)
