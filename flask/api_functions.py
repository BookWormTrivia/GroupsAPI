from sql_helper import _fetch_all_rows_for_query, execute_query
from random import randint

def getQuestionByGroup(group_id):
    query = '''
                SELECT * FROM questions
                WHERE group_id = {0}
            '''.format(group_id)
    rows = _fetch_all_rows_for_query(query)
    # For a new group with no rows
    if len(rows) == 0:
        return False
    out = []
    i = randint(0, len(rows) - 1)
    row = rows[i]
    question = {'question': row[2], 'correct_answer': row[3], 'incorrect_answers': row[4]}
    out.append(question)
    return out

def addGroup(group):
    query = '''
                INSERT INTO groups(
	               group_name)
	            VALUES ('{0}');
            '''.format(group)
    print(query)
    execute_query(query)

def addQuestion(group_name, question, correct_answer, incorrect_answers):
    group_id = getGroupIDByName(group_name)
    incorrect_str = '{'
    incorrect_str += incorrect_answers[0] + ', '
    incorrect_str += incorrect_answers[1] + ', '
    incorrect_str += incorrect_answers[2] + '}'
    query = '''
                INSERT INTO questions(
	                   group_id, question, correct_answer, incorrect_answers)
	            VALUES ('{0}', '{1}', '{2}', '{3}');
            '''.format(group_id, question, correct_answer, incorrect_str)
    print(query)
    execute_query(query)

def getGroupIDByName(group_name):
    query = '''
                SELECT id
                FROM groups
                WHERE group_name = '{0}'
            '''.format(group_name)
    print(query)
    rows = _fetch_all_rows_for_query(query)
    id = rows[0][0]
    return id
