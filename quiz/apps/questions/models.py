from django.db import models
from django.conf import settings
import django.contrib.auth

from django.views.generic.edit import CreateView

# Create your models here.
class Quiz (models.Model):
    quiz_name = models.CharField('Название викторины', max_length = 100)

    def __str__(self):
        return self.quiz_name

class Question (models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question_text = models.CharField('Текст вопроса', max_length = 500)
    variant_1 = models.CharField('Вариант 1', max_length = 200)
    variant_2 = models.CharField('Вариант 2', max_length = 200)
    variant_3 = models.CharField('Вариант 3', max_length = 200)
    correct_var = models.CharField('Правильный вариант', max_length=200)
    value = models.IntegerField("Ценность вопроса")



    def __str__(self):
        return self.question_text

class Score (models.Model):
    user = models.ForeignKey('auth.USER', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete = models.CASCADE)
    score = models.IntegerField('Счет пользователя в вопросе')

    def __str__(self):
        return str(self.user)