import sqlite3
import os.path


# root_dir = os.path.join(os.getcwd(), 'Django/quiz')
# db_path = os.path.join(root_dir, "db.sqlite3")
# with sqlite3.connect(db_path) as db:

#     user = 'admin'
#     cursor = db.cursor()
#     sql_record = """select questions_question.id, question_text, questions_score.score from questions_question 
#         left join questions_score on questions_question.id = questions_score.question_id
#         left join questions_quiz on questions_question.quiz_id = questions_quiz.id
#         LEFT JOIN auth_user on questions_score.user_id = auth_user.id
#         WHERE auth_user.id = '%s' and questions_quiz.id = '%s'""" %('2', '1')
#     cursor.execute(sql_record)
#     results = cursor.fetchall()
#     print(results)
    
#     db.close()



#     user = 'admin'
#     cursor = db.cursor()
#     sql_record = """SELECT questions_question.question_text, questions_question.id, questions_score.score, auth_user.username 
# FROM questions_score 
# LEFT JOIN questions_question ON questions_score.question_id = questions_question.id
# LEFT JOIN auth_user on questions_score.user_id = auth_user.id
# WHERE auth_user.username = '%s'""" %(user,)
#     cursor.execute(sql_record)
#     results = cursor.fetchall()
#     print(results)
#     #db.close()

root_dir = os.path.join(os.getcwd(), 'Django/quiz')
db_path = os.path.join(root_dir, "db.sqlite3")
with sqlite3.connect(db_path) as db:

    user = 'admin'
    cursor = db.cursor()
    sql_record = """select questions_question.id, question_text, questions_score.score from questions_question 
        left join questions_score on questions_question.id = questions_score.question_id
        left join questions_quiz on questions_question.quiz_id = questions_quiz.id
        LEFT JOIN auth_user on questions_score.user_id = auth_user.id
        WHERE questions_score.user_id = '%s' and questions_quiz.id = '%s'""" %('2', '1')

    cursor.execute(sql_record)
    results = cursor.fetchall()
    print(results)
    
    db.close()