"""Functional tests for the microservice (http tests) against the APIs"""
#import pytest
from flask import json
from service import app


def test_user_save():
    """Test user saving"""
    response = app.test_client().post(
        '/users/12345',
        data=json.dumps({'name': "test_user", 'b': "test_user_other_data"}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['completion']['user_id'] == '12345'


def test_greeter():
    """test greeter endpoint"""
    response = app.test_client().get(
        '/hello/nina'
        #data=json.dumps({'a': 1, 'b': 2}),
        #content_type='application/json',
    )

    data = response.get_data(as_text=True)

    assert response.status_code == 200
    assert data == "Hello nina!"
