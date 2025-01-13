from django.db import models

class BaseModel(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    
    class Meta:
        abstract = True
        verbose_name = "Базовая модель"
        verbose_name_plural = "Базовые модели"

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return f"Учитель {self.name}"


class Class(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название класса"
    )
    specialisation = models.CharField(
        max_length=100,
        verbose_name="Специализация"
    )
    students = models.ManyToManyField(
        'Student',
        related_name='enrolled_classes',
        verbose_name="Ученики"
    )

    def __str__(self):
        return f"Класс {self.name} - {self.specialisation}"

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Student(BaseModel):
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='students_in_class',
        verbose_name="Класс"
    )

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        return f"Ученик {self.name}"


class Parent(BaseModel):
    students = models.ManyToManyField(
        Student,
        related_name='parents',
        verbose_name="Дети"
    )

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    def __str__(self):
        return f"Родитель {self.name}"


class Homework(models.Model):
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='homeworks',
        verbose_name="Класс"
    )
    subject = models.CharField(
        max_length=100,
        verbose_name="Предмет"
    )
    homework = models.TextField(
        verbose_name="Домашнее задание"
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='homeworks',
        verbose_name="Учитель"
    )

    def __str__(self):
        return f"Домашнее задание по {self.subject}"

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"


class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name="Ученик"
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name="Учитель"
    )
    subject = models.CharField(
        max_length=100,
        verbose_name="Предмет"
    )
    grade = models.CharField(
        max_length=10,
        verbose_name="Оценка"
    )

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.grade}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
