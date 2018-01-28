import flask
import json
import config
import api_functions
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def test():
    return "BookWorm Trivia Groups API"

@app.route('/questions/<group_id>', methods=['GET'])
def questions_group(group_id):
    data = api_functions.getQuestionByGroup(group_id)
    out = {}
    out['results'] = data
    return json.dumps(out)

@app.route('/add/groups/', methods=['POST'])
def add_group():
    name = flask.request.form['group_name']
    api_functions.addGroup(name)
    return name

@app.route('/add/questions/', methods=['POST'])
def add_question():
    group_name = flask.request.form['group_name']
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
