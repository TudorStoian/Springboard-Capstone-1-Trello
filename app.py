# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:22:23 2020

@author: tudor
"""
#from class_file import class_name
from flask import Flask, render_template, redirect, session,url_for

from models import db,connect_db, User
from forms import RegisterForm, LoginForm



from werkzeug.exceptions import Unauthorized

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #Need this to be able to display flashing
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///springboard-trello"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "terces"


connect_db(app)
#db.drop_all()
#db.create_all()


@app.route("/" , methods = ['GET'])
def basic_display():
    
     return "Nothing here for now"