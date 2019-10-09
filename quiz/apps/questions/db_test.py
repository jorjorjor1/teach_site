import sqlite3
import os.path


root_dir = os.path.join(os.getcwd(), 'Django/quiz')
db_path = os.path.join(root_dir, "db.sqlite3")
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")

#     user = 'admin'
#     cursor = db.cursor()
#     sql_record = """INSERT INTO questions_score (default, value, question_id, auth_user.id)
# FROM questions_score 
# LEFT JOIN questions_question ON questions_score.question_id = questions_question.id
# LEFT JOIN auth_user on questions_score.user_id = auth_user.id
# WHERE auth_user.username = '%s'""" %(user,)
#     cursor.execute(sql_record)
#     results = cursor.fetchall()
#     print(results)
    
    #db.close()


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
