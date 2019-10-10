from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Quiz, Question, Score
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib import messages

import os.path
from django.db import connection

# Create your views here.
def main_screen(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'questions/main_page.html', {'quiz_list':quiz_list})

def questions_list(request):
    try:
        questions_list = Question.objects.all()
        return render(request, 'questions/question_list.html', {'questions_list': questions_list})


    except:
        raise Http404 ('Question_list не найден')


def question(request, question_id, quiz_id):

    try:
        quiz_num = Quiz.objects.get(id=quiz_id)
        question_setup = quiz_num.question_set.all()[question_id]
        questions_quant = int(quiz_num.question_set.count())
        next_question_id = int(question_id)+ 1
        prev_question_id = int(question_id) - 1
        variant_1 = question_setup.variant_1
        variant_2 = question_setup.variant_2
        variant_3 = question_setup.variant_3
        correct_var = question_setup.correct_var
        value = question_setup.value
        cursor = connection.cursor()
        user = request.user.get_username()
        sql_record_for_question = """SELECT questions_question.question_text, questions_score.score, auth_user.username 
        FROM questions_score 
        LEFT JOIN questions_question ON questions_score.question_id = questions_question.id
        LEFT JOIN auth_user on questions_score.user_id = auth_user.id
        WHERE auth_user.username = '%s' and questions_question.question_text = '%s'""" %(user, question_setup)
        cursor.execute(sql_record_for_question)
        total = cursor.fetchall()
        cursor.close()
        #print(user, total)




    except:
        raise Http404 ('Вопрос не найден')


    if request.POST.get('var') == correct_var:
        cursor = connection.cursor()
        user = request.user.get_username()
        sql_record = """SELECT questions_question.question_text, questions_score.score, auth_user.username 
        FROM questions_score 
        LEFT JOIN questions_question ON questions_score.question_id = questions_question.id
        LEFT JOIN auth_user on questions_score.user_id = auth_user.id
        WHERE auth_user.username = '%s' and questions_question.question_text = '%s'""" %(user, question_setup)
        cursor.execute(sql_record)
        results = cursor.fetchall()
        cursor.close()
        if user == "" and results == []:
            messages.add_message(request, messages.SUCCESS, 'Правильно!')
        elif user != "" and results == []:
            player = results[0][2]
            #print(player, value)
            messages.add_message(request, messages.SUCCESS, ('Правильно! Игрок {} получает {} очков').format(player, value))
            select_user_id = """select auth_user.id
            from auth_user
            WHERE auth_user.username = '%s'""" %(user,)
            cursor = connection.cursor()
            cursor.execute(select_user_id)
            user_id = cursor.fetchall()
            select_questions_id = """SELECT id from questions_question where question_text = '%s'""" %(question_setup,)
            cursor.execute(select_questions_id)
            quest_id = cursor.fetchall()
            inserting_score = """INSERT INTO questions_score  (score, question_id, user_id) values ('%s', '%s', '%s')""" %(value, quest_id[0][0], user_id[0][0],) 
            cursor.execute(inserting_score)
            inserted_score = cursor.fetchall()
            cursor.close()
        elif user != "" and results != []:
            player = results[0][2]
            messages.add_message(request, messages.SUCCESS, ('Правильно! Игрок {} отгадал вопрос раньше и получил {} очков').format(player, value))
        cursor.close()

        return render(request, 'questions/question.html',
                      {'question_setup': question_setup, "variant_1": variant_1, "variant_2": variant_2,
                       "variant_3": variant_3, 'correct_var':correct_var, 'next_question_id':next_question_id,
                       'prev_question_id':prev_question_id, 'quiz_id':quiz_id, 'questions_quant':questions_quant, 'value':value})


        #return HttpResponse(request.POST.get('var'))
    elif request.POST.get('var') != correct_var and request.POST.get('var') == variant_1 or request.POST.get('var') == variant_2 \
            or request.POST.get('var') == variant_3  :
        messages.add_message(request, messages.SUCCESS, 'Неправильно!')
        return render(request, 'questions/question.html',
                      {'question_setup': question_setup, "variant_1": variant_1, "variant_2": variant_2,
                       "variant_3": variant_3, 'correct_var':correct_var, 'next_question_id':next_question_id,
                       'prev_question_id':prev_question_id, 'quiz_id':quiz_id, 'questions_quant':questions_quant})

    else :
        return render(request, 'questions/question.html',
                      {'question_setup': question_setup, "variant_1": variant_1, "variant_2": variant_2,
                       "variant_3": variant_3, 'correct_var':correct_var, 'next_question_id':next_question_id,
                       'prev_question_id':prev_question_id, 'quiz_id':quiz_id, 'questions_quant':questions_quant})

    #return render(request, 'questions/question.html', {'question_setup': question_setup, "variant_1":variant_1, "variant_2":variant_2,"variant_3":variant_3})
#

def quiz_details(request, quiz_id):

    try:
        a = Quiz.objects.get(id=quiz_id)
        cursor = connection.cursor()
        user = request.user.get_username()
        #x = a.question_set.all() 
        select_questions_list = """select questions_question.id, questions_question.question_text from questions_question where questions_question.quiz_id = '%s'""" %(quiz_id)
        cursor.execute(select_questions_list)
        quest_list = cursor.fetchall()
        x = []
        for quest in quest_list:
            x.append(quest)
        #print(x)
        
        select_user_id_in_quiz = """select auth_user.id
                from auth_user
                WHERE auth_user.username = '%s'""" %(user,)
        cursor.execute(select_user_id_in_quiz)
        user_id = cursor.fetchall()

        select_done_score = """select questions_question.id, question_text, questions_score.score from questions_question 
        left join questions_score on questions_question.id = questions_score.question_id
        left join questions_quiz on questions_question.quiz_id = questions_quiz.id
        LEFT JOIN auth_user on questions_score.user_id = auth_user.id
        WHERE auth_user.id = '%s' and questions_quiz.id = '%s'""" %(user_id[0][0], quiz_id)
        cursor.execute(select_done_score)
        raw_result = cursor.fetchall()
        #print(raw_result)
        done_score = []
        new_data = []
        id_checked =[]
        for result in raw_result:
            done_score.append(result)
        #print(done_score)
        for para in done_score:
            if para[2] != "" and para[0] not in id_checked:
                diction = [para[0], para[1], para[2]]
                new_data.append(diction)
                id_checked.append(para[0])
        for pair in x:
            if pair[0] not in id_checked:
                diction2 = [pair[0], pair[1]]
                new_data.append(diction2)
                id_checked.append(pair[0])

            

        print(new_data)
                    



    except:
        raise Http404 ('Вопрос не найден')

    return render(request, 'questions/question_list.html', {'x': x, 'new_data':new_data})



def login_user(request):
    #logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'questions/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'questions/signup.html', {'form': form})


def LogoutView(request):
    logout(request)

    # После чего, перенаправляем пользователя на главную страницу.
    return HttpResponseRedirect("/")

