import pandas as pd

from flask import Flask, request, jsonify

import os

app = Flask(__name__)

app.config['DATABASE_FOLDER'] = "/Users/theobensoussan/webimmo/" #Here you can change the path of the database files


@app.route('/api-web-immo/v1.0/create_user/', methods=['POST']) #POST request to create our user database as a .csv file
def create_new_user():
    if request.method == 'POST':

        info = request.args.to_dict()

        if 'user_id' in info: #The user chooses his user_id
            user_id = info['user_id']

            if 'password' in info: #The user chooses his password
                password = info['password']
            else:
                return "ERROR : MISSING PASSWORD ARGUMENT. "
        else:
            return "ERROR : MISSING USER_ID ARGUMENT. "

        last_name = info['last_name']
        first_name = info['first_name']
        birth_date = info['birth_date']

        if os.path.isfile('{}/base_user.csv'.format(app.config['DATABASE_FOLDER'])):
            df = pd.read_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

            if user_id in df['user_id'].values:
                return "We are sorry, this user_id already exists. Please create a new one. "
            else:
                df.loc[df.shape[0]] = [user_id, password, last_name, first_name, birth_date]
                df.to_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), index=False, sep='|')
                return "Thank you {}! Your user account has been successfully created. ".format(first_name)
        else:
            df = pd.DataFrame(columns=['user_id', 'password', 'last_name', 'first_name', 'birth_date'])
            df.loc[0] = [user_id, password, last_name, first_name, birth_date]
            df.to_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), index=False, sep='|')

            return "Thank you {}! Your user account has been successfully created. ".format(first_name)

    else:
        return "ERROR : WRONG METHOD. "


@app.route('/api-web-immo/v1.0/create_good/', methods=['POST']) #POST request to create our good database, accessible only by authenticated users
def create_new_good():
    if request.method == 'POST':

        info = request.args.to_dict()

        if 'user_id' in info:
            user_id = info['user_id']

            if 'password' in info:
                password = info['password']
            else:
                return "ERROR : MISSING PASSWORD ARGUMENT. "
        else:
            return "ERROR : MISSING USER_ID ARGUMENT. "

        if os.path.isfile('{}/base_user.csv'.format(app.config['DATABASE_FOLDER'])):
            dfu = pd.read_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

            if user_id in dfu['user_id'].values:  #User must have created an account before creating a good

                index_user_id = dfu[dfu['user_id'] == user_id].index[0]

                if password == dfu.loc[index_user_id, 'password']: #Password check, to ensure that the user is authenticated

                    good_id = info['good_id']
                    good_name = info['good_name']
                    description = info['description']
                    good_type = info['type']
                    city = info['city']
                    rooms = info['rooms']
                    characteristics = info['characteristics']

                    if os.path.isfile('{}/base_good.csv'.format(app.config['DATABASE_FOLDER'])):
                        dfg = pd.read_csv('{}/base_good.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

                        if good_id in dfg['good_id'].values:
                            return "We are sorry, this good_id already exists. Please create a new one. "
                        else:
                            dfg.loc[dfg.shape[0]] = [good_id, good_name, description, good_type, city, rooms,
                                                     characteristics, user_id]
                            dfg.to_csv('{}/base_good.csv'.format(app.config['DATABASE_FOLDER']), index=False, sep='|')
                            return "Thank you! Your good {} has been successfully created. ".format(good_name)
                    else:
                        dfg = pd.DataFrame(
                            columns=['good_id', 'good_name', 'description', 'type', 'city', 'rooms', 'characteristics',
                                     'landlord'])
                        dfg.loc[0] = [good_id, good_name, description, good_type, city, rooms, characteristics, user_id]
                        dfg.to_csv('{}/base_good.csv'.format(app.config['DATABASE_FOLDER']), index=False, sep='|')

                        return "Thank you! Your good {} has been successfully created. ".format(good_name)
                else:
                    return "ERROR: WRONG PASSWORD FOR {}. ".format(user_id)
            else:
                return "We are sorry. You need a user account to create a good. "
        else:
            return "We are sorry. You need to create a user account to create a good. "

    else:
        return "ERROR : WRONG METHOD. "


@app.route('/api-web-immo/v1.0/edit_user/', methods=['PUT']) #PUT request to edit/update user's information, if and only if user exists
def edit_user():
    if request.method == 'PUT':

        info = request.args.to_dict()

        if 'user_id' in info:
            user_id = info['user_id']

            if 'password' in info:
                password = info['password']
            else:
                return "ERROR : MISSING PASSWORD ARGUMENT"
        else:
            return "ERROR : MISSING USER_ID ARGUMENT. "

        last_name = info['last_name']
        first_name = info['first_name']
        birth_date = info['birth_date']

        if os.path.isfile('{}/base_user.csv'.format(app.config['DATABASE_FOLDER'])):
            df = pd.read_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

            if user_id in df['user_id'].values: #User must have created an account before editing his information
                index_user_id = df[df['user_id'] == user_id].index[0]

                if password == df.loc[index_user_id, 'password']: #Password check, to ensure that the user is authenticated

                    df.loc[index_user_id] = [user_id, password, last_name, first_name, birth_date]
                    df.to_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), index=False, sep='|')

                    return "Thank you {}! Your account has been updated successfully. ".format(user_id)
                else:
                    return "ERROR: WRONG PASSWORD FOR {} ".format(user_id)
            else:
                return "We are sorry. You need a user account to edit it. "
        else:
            return "There is no user database yet. Feel free to create one. "
    else:
        return "ERROR : WRONG METHOD. "


@app.route('/api-web-immo/v1.0/edit_good/', methods=['PUT']) #PUT request to edit/update good's information, if and only if good exists and 'good_id' matches 'user_id'
def edit_good():
    if request.method == 'PUT':

        info = request.args.to_dict()

        if 'user_id' in info:
            user_id = info['user_id']

            if 'password' in info:
                password = info['password']
            else:
                return "ERROR : MISSING PASSWORD ARGUMENT. "
        else:
            return "ERROR : MISSING USER_ID ARGUMENT. "

        if os.path.isfile('{}/base_user.csv'.format(app.config['DATABASE_FOLDER'])):
            dfu = pd.read_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

            if user_id in dfu['user_id'].values: #User must have created an account before editing a good

                index_user_id = dfu[dfu['user_id'] == user_id].index[0]

                if password == dfu.loc[index_user_id, 'password']: #Password check, to ensure that the user is authenticated

                    good_id = info['good_id']
                    good_name = info['good_name']
                    description = info['description']
                    good_type = info['type']
                    city = info['city']
                    rooms = info['rooms']
                    caracteristics = info['caracteristics']

                    if os.path.isfile('{}/base_good.csv'.format(app.config['DATABASE_FOLDER'])):
                        dfg = pd.read_csv('{}/base_good.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

                        if good_id in dfg['good_id'].values: #The good must exists in order to edit it

                            index_good_id = dfg[dfg['good_id'] == good_id].index[0]

                            if user_id == dfg.loc[index_good_id, 'landlord']: #The good must belong to the authenticated user to edit it

                                dfg.loc[index_good_id] = [good_id, good_name, description, good_type, city, rooms,
                                                     caracteristics, user_id]
                                dfg.to_csv('{}/base_good.csv'.format(app.config['DATABASE_FOLDER']), index=False, sep='|')

                                return "Thank you! Your good {} has been updated successfully. ".format(good_id)
                            else:
                                return "We are sorry. This good_id does not match your user_id. "
                        else:
                            return "We are sorry. Good_id {} does not exist. ".format(good_id)
                    else:
                        return "There is no good database yet. Feel free to create one. "
                else:
                    return "ERROR: WRONG PASSWORD FOR {}. ".format(user_id)
            else:
                return "We are sorry. You need a user account to edit a good or create one. "
        else:
            return "There is no user database yet. Feel free to create one. "

    else:
        return "ERROR : WRONG METHOD. "


@app.route('/api-web-immo/v1.0/consult_good/', methods=['GET']) #GET method to return the user the list of goods of a particular city
def consult_good():
    if request.method == 'GET':

        info = request.args.to_dict()
        user_id = info['user_id']
        password = info['password']

        if os.path.isfile('{}/base_user.csv'.format(app.config['DATABASE_FOLDER'])):
            dfu = pd.read_csv('{}/base_user.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

            if user_id in dfu['user_id'].values:
                index_user_id = dfu[dfu['user_id'] == user_id].index[0]

                if password == dfu.loc[index_user_id, 'password']:

                    if os.path.isfile('{}/base_good.csv'.format(app.config['DATABASE_FOLDER'])):
                        dfg = pd.read_csv('{}/base_good.csv'.format(app.config['DATABASE_FOLDER']), sep='|')

                        city = info['city']
                        dfg_c = dfg[dfg['city'] == city] #We create a new data frame that is filtered with the key 'city'

                        return jsonify(dfg_c.to_dict('index')) #jsonify will return the list of goods matching the city the user chose

                    else:
                        return "There is no good in our database. Please create one. "

                else:
                    return "ERROR: WRONG PASSWORD FOR {}. ".format(user_id)
            else:
                return "You need a user account to access good database. "
        else:
            return "You need to create a user account to access good database. "
    else:
        return "ERROR : WRONG METHOD. "

if __name__ == '__main__':
    #    app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=5000)


#curl -X POST "http://localhost:5000/api-web-immo/v1.0/create_user/?user_id=theobens&password=arcane&first_name=theo&last_name=bensoussan&birth_date=01101992"
#curl -X POST "http://localhost:5000/api-web-immo/v1.0/create_good/?user_id=theobens&password=arcane&good_id=mygood1&good_name=quietstudio&description=20m2studio&type=studio&city=paris&rooms=2&characteristics=parking"

#curl -X PUT "http://localhost:5000/api-web-immo/v1.0/edit_user/?user_id=theobens&password=arcane&first_name=thomas&last_name=bricot&birth_date=01101991"
#curl -X PUT "http://localhost:5000/api-web-immo/v1.0/edit_good/?user_id=theobens&password=arcane&good_id=mygood1&good_name=noisystudio&description=25m2studio&type=studio&city=paris&rooms=2&characteristics=none"

#curl -X GET "http://localhost:5000/api-web-immo/v1.0/consult_good/?user_id=theobens&password=arcane&city=paris