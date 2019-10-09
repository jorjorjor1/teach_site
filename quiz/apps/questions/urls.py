from django.urls import path, include



urlpatterns = [
    path('', views.question_list, name = 'question_list'),
    path('<int:quiz_id>/', views.quiz_details, name = 'quiz_details'),
    #path('<int:quiz_id>/<int:question_id>/', views.question, name = 'question'),
]
