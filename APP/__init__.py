# coding:utf8
from flask import Flask
import  os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

#import pymysql
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:weilan88@127.0.0.1:8889/movie"
app.config['SECRET_KEY'] = "3a14c074e62446e798e9210b16a5c319"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#全局变量
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")

db = SQLAlchemy(app)


from APP.home import home as home_blueprint
app.register_blueprint(home_blueprint)


