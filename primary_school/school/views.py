from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404


school_data = {
    'teachers': {
        1: {
            'id': 1,
            'name': "Александр Викторович",
            'subjects': ["Математика", "Информатика"],
            'classes': [1, 2],
            'grades': [
                {'student_id': 1, 'subject': "Математика", 'grade': "4"},
                {'student_id': 2, 'subject': "Русский", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Математика", 'homework': "Изучить текст"},
                {'class_id': 2, 'subject': "Информатика", 'homework': "Подготовиться к контрольной"},
            ],
        },
        2: {
            'id': 2,
            'name': "Мария Игоревна",
            'subjects': ["Русский язык", "Литература"],
            'classes': [2],
            'grades': [
                {'student_id': 2, 'subject': "Математика", 'grade': "5"},
                {'student_id': 1, 'subject': "Русский", 'grade': "4"}
            ],
            'homeworks': [
                {'class_id': 2, 'subject': "Русский язык", 'homework': "Изучить лекцию по русскому языку"}
            ],
        },
        3: {
            'id': 3,
            'name': "Олег Николаевич",
            'subjects': ["Физика", "Химия"],
            'classes': [1],
            'grades': [
                {'student_id': 1, 'subject': "Физика", 'grade': "5"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Физика", 'homework': "Решить задачи по теме \"Механика\""}
            ],
        },
        4: {
            'id': 4,
            'name': "Ирина Александровна",
            'subjects': ["История", "Обществознание"],
            'classes': [2],
            'grades': [
                {'student_id': 2, 'subject': "История", 'grade': "4"},
            ],
            'homeworks': [
                {'class_id': 2, 'subject': "История", 'homework': "Прочитать главу 3 учебника"}
            ],
        },
        5: {
            'id': 5,
            'name': "Елена Дмитриевна",
            'subjects': ["География", "Экономика"],
            'classes': [1, 2],
            'grades': [
                {'student_id': 1, 'subject': "География", 'grade': "5"},
                {'student_id': 2, 'subject': "Экономика", 'grade': "3"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "География", 'homework': "Нарисовать карту России"},
                {'class_id': 2, 'subject': "Экономика", 'homework': "Подготовить презентацию о спросе и предложении"}
            ],
        },
        6: {
            'id': 6,
            'name': "Виктория Павловна",
            'subjects': ["Биология", "Экология"],
            'classes': [1],
            'grades': [
                {'student_id': 1, 'subject': "Биология", 'grade': "4"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Биология", 'homework': "Подготовить гербарий"}
            ],
        },
        7: {
            'id': 7,
            'name': "Игорь Александрович",
            'subjects': ["Музыка", "ИЗО"],
            'classes': [1, 2],
            'grades': [
                {'student_id': 2, 'subject': "Музыка", 'grade': "5"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Музыка", 'homework': "Разучить песню \"Катюша\""}
            ],
        },
        8: {
            'id': 8,
            'name': "Анатолий Евгеньевич",
            'subjects': ["Физкультура", "Труд"],
            'classes': [2],
            'grades': [],
            'homeworks': [
                {'class_id': 2, 'subject': "Труд", 'homework': "Сделать поделку из бумаги"}
            ],
        },
        9: {
            'id': 9,
            'name': "Максим Валерьевич",
            'subjects': ["Математика", "Информатика"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "Математика", 'grade': "5"},
                {'student_id': 5, 'subject': "Информатика", 'grade': "4"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "Математика", 'homework': "Решить задачи на умножение"},
                {'class_id': 3, 'subject': "Информатика", 'homework': "Написать программу на Python"},
            ],
        },
        10: {
            'id': 10,
            'name': "Екатерина Сергеевна",
            'subjects': ["Русский язык", "Литература"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "Русский язык", 'grade': "4"},
                {'student_id': 5, 'subject': "Литература", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "Русский язык", 'homework': "Изучить правило о мягком знаке"},
                {'class_id': 3, 'subject': "Литература", 'homework': "Прочитать сказку \"Морозко\""},
            ],
        },
        11: {
            'id': 11,
            'name': "Никита Викторович",
            'subjects': ["История", "Обществознание"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "История", 'grade': "3"},
                {'student_id': 5, 'subject': "Обществознание", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "История", 'homework': "Выучить даты из главы 2"},
                {'class_id': 3, 'subject': "Обществознание", 'homework': "Написать эссе на тему \"Что такое семья\""},
            ],
        },
        12: {
            'id': 12,
            'name': "Дмитрий Андреевич",
            'subjects': ["Химия", "Физика"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "Химия", 'grade': "4"},
                {'student_id': 5, 'subject': "Физика", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "Химия", 'homework': "Подготовить отчет о проведенном эксперименте"},
                {'class_id': 3, 'subject': "Физика", 'homework': "Рассчитать скорость движения тела"},
            ],
        },
    },
    'classes': {
        1: {
            'id': 1,
            'name': "1-А",
            'students': [1, 2],
            'homeworks': [
                {'subject': "Математика", 'homework': "Изучить текст"},
                {'subject': "Математика", 'homework': "Решить задачи по математике"},
            ],
            'specialisation': "математическая"
        },
        2: {
            'id': 2,
            'name': "2-Б",
            'students': [3],
            'homeworks': [
                {'subject': "Информатика", 'homework': "Подготовиться к контрольной"},
                {'subject': "Русский язык", 'homework': "Изучить лекцию по русскому языку"},
            ],
            'specialisation': "гуманитарная"
        },
        3: {
            'id': 3,
            'name': "3-А",
            'students': [4, 5],
            'homeworks': [
                {'subject': "Математика", 'homework': "Решить задачи на умножение"},
                {'subject': "Информатика", 'homework': "Написать программу на Python"},
            ],
            'specialisation': "техническая"
        },
        4: {
            'id': 4,
            'name': "3-Б",
            'students': [6],
            'homeworks': [
                {'subject': "Русский язык", 'homework': "Изучить правило о мягком знаке"},
                {'subject': "Литература", 'homework': "Прочитать сказку \"Морозко\""},
            ],
            'specialisation': "искусствоведческая"
        }
    },
    "students": {   
        1: {
        'id': 1,
        'name': "Иван Петров",
        'class_id': 1,
        'grades': [
            {'teacher_id': 1, 'subject': "Математика", 'grade': "4"},
            {'teacher_id': 2, 'subject': "Русский язык", 'grade': "4"}
        ],
        'homeworks': [
                {'subject': "Математика", 'homework': "Решить 5 задач"},
                {'subject': "Русский язык", 'homework': "Написать сочинение"},
        ],
    },
    2: {
        'id': 2,
        'name': "Анна Смирнова",
        'class_id': 1,
        'grades': [
            {'teacher_id': 1, 'subject': "Математика", 'grade': "5"},
            {'teacher_id': 2, 'subject': "Русский язык", 'grade': "5"}
        ],
        'homeworks': [
                {'subject': "Информатика", 'homework': "Изучить алгебру логики"},
                {'subject': "Русский язык", 'homework': "Прописи"},
        ],
    },
    3: {
        'id': 3,
        'name': "Дмитрий Иванов",
        'class_id': 2,
        'grades': [
            {'teacher_id': 1, 'subject': "Математика", 'grade': "5"},
            {'teacher_id': 2, 'subject': "Русский язык", 'grade': "4"}
        ]
    },
    4: {
        'id': 4,
        'name': "Мария Орлова",
        'class_id': 3,
        'grades': [
            {'teacher_id': 9, 'subject': "Математика", 'grade': "5"},
            {'teacher_id': 10, 'subject': "Русский язык", 'grade': "4"}
        ]
    },
    5: {
        'id': 5,
        'name': "Алексей Григорьев",
        'class_id': 3,
        'grades': [
            {'teacher_id': 9, 'subject': "Математика", 'grade': "4"},
            {'teacher_id': 10, 'subject': "Литература", 'grade': "5"}
        ]
    },
    6: {
        'id': 6,
        'name': "Елена Левина",
        'class_id': 4,
        'grades': [
            {'teacher_id': 11, 'subject': "История", 'grade': "3"},
            {'teacher_id': 12, 'subject': "Физика", 'grade': "5"}
        ]
    }
    },
        'parents': {
        1: {
            'id': 1,
            'name': "Александр Петров",
            'students': [1],
        },
        2: {
            'id': 2,
            'name': "Дмитрий Смирнов",
            'students': [2],
        },
    },
}





def index(request):
    return render(request, 'pages/home.html')

def class_list(request):
    template = 'pages/class_list.html'
    classes = sorted(school_data['classes'].values(), key=lambda x: x['name'])
    context = {
        'classes': classes
    }
    return render(request, template, context)


def teacher_list(request):
    template = 'pages/teacher_list.html'
    teachers = school_data['teachers'].values()
    context = {
        'teachers': teachers
    }
    return render(request, template, context)


def get_students_list(teacher):
    students_list = []
    for class_id in teacher['classes']:
        class_obj = school_data['classes'].get(class_id)
        if class_obj:
            for student_id in class_obj['students']:
                student = school_data['students'].get(student_id)
                if student:
                    students_list.append(student['name'])
    return students_list


def teacher_dashboard(request, teacher_id):
    template = 'pages/teacher_dashboard.html'
    teacher = school_data['teachers'].get(teacher_id)
    if not teacher:
        return HttpResponse("Учитель не найден", status=404)

    homeworks = teacher.get('homeworks', [])
    grades = teacher.get('grades', [])
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
    parent = school_data['parents'].get(parent_id)
    if parent is None:
        raise Http404("Студент не найден. Пожалуйста, проверьте, что ID корректен и студент существует.")

    students = [school_data['students'][sid] for sid in parent['students']]

    if not students:
        students_details = {
            'name': 'Нет детей',
            'homeworks': [],
            'grades': [],
        }
    else:
        students_details = []
        for student in students:
            homeworks = student['homeworks']
            grades = student['grades']

            students_details.append({
                'name': student['name'],
                'homeworks': homeworks,
                'grades': grades,
            })

    context = {
        'parent': parent,
        'students_details': students_details,
    }
    return render(request, template, context)


students_by_id = {student['id']: student for student in school_data['students'].values()}


def student_dashboard(request, student_id):
    template = 'pages/student_dashboard.html'
    if not isinstance(student_id, int):
        raise Http404(f'Некорректный параметр student_id: {student_id}')
    student = students_by_id.get(student_id)
    if student is None:
        raise Http404(f'Студент с student_id {student_id} не найден')

    context = {
        'student': student,
        'homeworks': student.get('homeworks', []),
        'grades': student.get('grades', []),
    }
    return render(request, template, context)

