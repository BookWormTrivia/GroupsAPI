import flask
import json
import config
import api_functions
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

base_url = 'http://www.bookwormtrivia.com.s3-website.us-east-2.amazonaws.com'

@app.route('/')
def test():
    return "BookWorm Trivia Groups API"

@app.route('/questions/id/<group_id>/', methods=['GET'])
def questions_group_byID(group_id):
    data = api_functions.getQuestionByGroup(group_id)
    out = {}
    out['results'] = data
    return json.dumps(out)

@app.route('/questions/name/<group_name>/', methods=['GET'])
def questions_group_byName(group_name):
    group_id = api_functions.getGroupIDByName(group_name)
    data = api_functions.getQuestionByGroup(group_id)
    if not data:
        return 'No Questions'
    out = {}
    out['results'] = data
    return json.dumps(out)

@app.route('/add/groups/', methods=['POST'])
def add_group():
    name = flask.request.form['group_name']
    api_functions.addGroup(name)
    return flask.redirect(base_url + '/groups.html')

@app.route('/add/questions/', methods=['POST'])
def add_question():
    group_name = flask.request.form['group_name']
    print('group name: ', group_name)
    question = flask.request.form['question']
    correct = flask.request.form['correct_answer']
    incorrect = list()
    incorrect.append(flask.request.form['incorrect_1'])
    incorrect.append(flask.request.form['incorrect_2'])
    incorrect.append(flask.request.form['incorrect_3'])

    api_functions.addQuestion(group_name, question, correct, incorrect)

    return 'Posted'

if __name__ == '__main__':
    app.run(config.api_host, config.api_port)
