import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
with sqlite3.connect(db_path) as db:

    user = 'admin'
    cursor = db.cursor()
    sql_record = """SELECT questions_question.question_text, questions_question.id, questions_score.score, auth_user.username 
FROM questions_score 
LEFT JOIN questions_question ON questions_score.question_id = questions_question.id
LEFT JOIN auth_user on questions_score.user_id = auth_user.id
WHERE auth_user.username = '%s' and questions_question.question_text = '%s'""" %(user, 'Как дела?') 
    cursor.execute(sql_record)
    results = cursor.fetchall()
    print(results)
    #db.close()


#             db_path = os.path.join(BASE_DIR, "db.sqlite3")
#         with sqlite3.connect(db_path) as db:
#             cursor = db.cursor()
#             sql_record = """SELECT questions_score.score 
# FROM questions_score 
# LEFT JOIN questions_question ON questions_score.question_id = questions_question.id
# LEFT JOIN auth_user on questions_score.user_id = auth_user.id
# WHERE questions_question.question_text = '%s'""" %(question_setup)
#             cursor.execute(sql_record)
#             results = cursor.fetchall()
