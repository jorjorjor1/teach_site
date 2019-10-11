from django.contrib import admin

# Register your models here.
from .models import Question, Quiz



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz_id')

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('username', 'question')

admin.site.register(Question, QuestionAdmin)

admin.site.register(Quiz)



