import sys
from flask.json import JSONEncoder
from bson import json_util, ObjectId
from configparser import ConfigParser
from flask import Flask,render_template,request,jsonify

from python_files import auth, api_calls, helper

from python_files.blueprint_mongodb.mongodb_bp import bp_mongodb
from datetime import datetime

import json
from python_files.blueprint_mongodb import db

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, float):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)

if __name__=='__main__':
    app=Flask(__name__)
    config=ConfigParser()
    config.read('configuration.cfg')

    app.json_encoder=MongoJsonEncoder

    #Reading of MongoDB data configuration
    app.config['DB_SRV']=config['db_credentials']['DB_SRV']
    app.config['DB_NAME']=config['db_credentials']['DB_NAME']
    app.config['DB_USERNAME']=config['db_credentials']['DB_USERNAME']
    app.config['DB_PASSWORD']=config['db_credentials']['DB_PASSWORD']
    
    
    app.register_blueprint(bp_mongodb,url_prefix='/mongo')
    
    
    @app.route('/')
    def index():
        return render_template('index.html',title="Index Page for my site",message_count=0,conv=convlist,no_conversation_list=True)
        
    
    app.run(debug=True)