"""Entry point of our microservice. API endpoints (routes) are defined here.
 """

#pylint: disable=unused-import
import logging as log
import uuid

from flask import Flask, request, jsonify, Response
from src import handlers, model

# pylint: disable=invalid-name
app = Flask(__name__)


@app.route('/hello/<name>', methods=['GET'])
def say_hello(name):
    """ Greeter Endpoint"""
    resp = handlers.greeter(name)
    return Response(resp, mimetype='plain/text')

# For more sophisticated forms in Flask, see:
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
@app.route('/users', defaults={'user_id': ""}, methods=['POST'])
@app.route('/users/<user_id>', methods=['POST'])
def update_user(user_id):
    """Endpoint that creates or saves user in Redis database"""
    # Note 'force=True' ignores mime-type=app/json requirement default in Flask
    user = request.get_json(force=True)

    resp = handlers.save_user(user, user_id)
    return jsonify(resp)


def init():
    """Init routine for the microservice"""
    uuid.uuid1() # prime the uuid generator at startup

if __name__ == '__main__':
    init()

    app.run(debug=True, host='0.0.0.0')
