# -*- coding: utf-8 -*-
#!/usr/bin/env python

# initiate flask instance dulu
import os
from flask import Flask, render_template, json, request, g
from flask_cors import CORS
from helpers.response_builder import resp


ENV = os.getenv('env_omni','Config')
app = Flask(__name__,static_folder = 'static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object('config.main.%s' % (ENV))


# APP blueprints
from app.rest_api.controllers import rest_controller

#from helpers.mysql_connect import Database


@app.errorhandler(404)
def page_not_found(e):
    
    return resp(404)

@app.errorhandler(405)
def page_not_found(e):

    return resp(405)

@app.errorhandler(500)
def page_not_found(e):
    
    return resp(500)

# database connection management
# @app.before_request
# # @limit()
# def before_request():
#     connection = Database()
#     g.cursor = connection.query
#     g.cursor('SET NAMES UTF8MB4')
#     g.db = connection.db

# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()


# import application modules
app.register_blueprint(rest_controller)


