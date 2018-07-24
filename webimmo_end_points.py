import pandas as pd

from flask import Flask, request

app = Flask(__name__)

@app.route('/api-web-immo/v1.0/create_user/', methods=['POST']) #POST request to create our user database as a .csv file
def create_new_user():
    if request.method == 'POST':

        info = request.args.to_dict()
        user_id = info['user_id']
        password = info['password']
        last_name = info['last_name']
        first_name = info['first_name']
        birth_date = info['birth_date']
    else:
        return 'ERROR : WRONG METHOD'


@app.route('/api-web-immo/v1.0/create_good/', methods=['POST']) #POST request to create our good database, accessible only by users
def create_new_good():
    if request.method == 'POST':

        info = request.args.to_dict()
        user_id = info['user_id']
        password = info['password']
        good_id = info['good_id']
        good_name = info['good_name']
        description = info['description']
        good_type = info['type']
        city = info['city']
        rooms = info['rooms']
        caracteristics = info['caracteristics']
    else:
        return 'ERROR : WRONG METHOD'


@app.route('/api-web-immo/v1.0/edit_user/', methods=['PUT']) #PUT request to edit/update user's information, if and only if user exists
def edit_user():
    if request.method == 'PUT':

        info = request.args.to_dict()
        user_id = info['user_id']
        password = info['password']
        last_name = info['last_name']
        first_name = info['first_name']
        birth_date = info['birth_date']
    else:
        return 'ERROR : WRONG METHOD'


@app.route('/api-web-immo/v1.0/edit_good/', methods=['PUT']) #PUT request to edit/update good's information, if and only if good exists and 'good_id' matches 'user_id'
def edit_good():
    if request.method == 'PUT':

        info = request.args.to_dict()
        user_id = info['user_id']
        password = info['password']
        good_id = info['good_id']
        good_name = info['good_name']
        description = info['description']
        good_type = info['type']
        city = info['city']
        rooms = info['rooms']
        caracteristics = info['caracteristics']
    else:
        return 'ERROR : WRONG METHOD'


@app.route('/api-web-immo/v1.0/consult_good/', methods=['GET']) #GET method to return the user the list of goods of a particular city
def consult_good():
    if request.method == 'GET':

        info = request.arg.to_dict()
        user_id = info['user_id']
        password = info['password']
        city = info['city']
    else:
        return 'ERROR : WRONG METHOD'
