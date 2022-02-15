# IMPORT
import os
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv, find_dotenv

# loading environment variables
load_dotenv(find_dotenv())

# APP SETUP
app = Flask(__name__)
# enable resource sharing between frontend and server
CORS(app)

# DB
mongo = PyMongo()
app.config['MONGO_URI'] = os.getenv('MONGODB_ATLAS_DB_LINK')

mongo.init_app(app)

# ROUTES
@app.route('/hello', methods=['GET'])
def hello():
	return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)
