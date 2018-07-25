# webimmo
project for arcane

1st: I chose to use a csv database (text file that can be exported as an excel file easy to use).

      I import pandas library to use dataframes. I will convert them as csv files.
      There will be two databases, one for the users and one for the goods. 
      Each user is unique, has a unique user_id and must log in with a password to access features such as creating, updating or consulting a good.
      Each good is unique, has a unique good_id and user_id (landlord). The only search key when you search a good among the database is the city.

2nd: Stating the app endpoints (create functions, edit functions and consult function).

      Create functions will be POST requests.
      Edit functions will be PUT requests.
      The consult function will be a GET request.

3rd: Coding the functions using the following requirements.

      Each unique user can create/update his first name, his last name and his birth date.
      Each unique user can create/update a good with new information such as the name, the description, the type, the number of rooms, the city and the characteristics. Only the good_id and the landlord (user_id) cannot be updated. I chose no specific variable type for the arguments.
      A user can only consult the list of goods of a particular city. He cannot access to the whole database.
      
      I added an authentication process with user_id and password to allow a user to update his information and to create or update his good(s) information. If a user does not have an account, he cannot use these functions.
      
4th: Opening the console and type curl commands with request agruments (INSTRUCTIONS TO RUN THE WEB API ON LOCALHOST)

      WARNING: Change the directory path for the database csv files that you want to create. Me, I've put "app.config['DATABASE_FOLDER'] = "/Users/theobensoussan/webimmo/" as a path."
      Open your terminal and type the command to run your app on localhost. Me, I've type "python3.7 /Users/theobensoussan/Library/Preferences/PyCharm2018.1/scratches/venv/webimmo_all_functions.py". The app is now running.
      Then open a new console and start testing the app with curl commands. Depending on what function you want to execute.
      As you cannot edit or consult a good without any user or good database you can either create ones with the create functions or use the csv files given in the git repository. You must put these files in the database folder mentioned above.
      
      Here are the curl commands that you should type in your console in order to execute the functions of the web api :
      
      curl -X POST "http://localhost:5000/api-web-immo/v1.0/create_user/?user_id=theobens&password=arcane&first_name=theo&last_name=bensoussan&birth_date=01101992" to CREATE a user
      curl -X POST "http://localhost:5000/api-web-immo/v1.0/create_good/?user_id=theobens&password=arcane&good_id=mygood1&good_name=quietstudio&description=20m2studio&type=studio&city=paris&rooms=2&characteristics=parking" to create a good
      
      curl -X PUT "http://localhost:5000/api-web-immo/v1.0/edit_user/?user_id=theobens&password=arcane&first_name=thomas&last_name=bricot&birth_date=01101991" to UPDATE user's information
      curl -X PUT "http://localhost:5000/api-web-immo/v1.0/edit_good/?user_id=theobens&password=arcane&good_id=mygood1&good_name=noisystudio&description=25m2studio&type=studio&city=paris&rooms=2&characteristics=none" to UPDATE information about a user's good
      
      curl -X GET "http://localhost:5000/api-web-immo/v1.0/consult_good/?user_id=theobens&password=arcane&city=paris to CONSULT a list of goods (I chose to display a python dictionary to the user) of a specific city
      
      


