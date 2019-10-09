from django.contrib import admin

# Register your models here.
from .models import Question, Quiz, Score


admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Score)


