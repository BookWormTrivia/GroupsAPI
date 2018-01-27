import flask
import json
import config
import api_data
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def test():
    return "BookWorm Trivia Groups API"

@app.route('/questions/<group_id>', methods=['GET'])
def questions_group(group_id):
    data = api_data.getQuestionsByGroup(group_id)
    out = {}
    out['results'] = data
    return json.dumps(out)

@app.route('/add/groups/', methods=['POST'])
def add_group():
    name = flask.request.form['group_name']
    print(name)
    api_data.addGroup(name)
    return name

if __name__ == '__main__':
    app.run(config.api_host, config.api_port)
