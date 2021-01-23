from flask import Blueprint, request, send_from_directory
from app.rest_api.models import Database
from helpers.response_builder import resp
from helpers.validator import client_checker
import os
from app import app


rest_controller = Blueprint('rest_controller', __name__, url_prefix='/omniapi')
#---------------------------------------------------------------
@rest_controller.route('/welcome', methods=['GET'])
@client_checker(no_auth=True) #used for validating user access
def welcome(**kwargs):

    return 'welcome'

#---------------------------------------------------------------
@rest_controller.route('/get_file', methods=['GET'])
@client_checker(no_auth=True) #used for validating user access
def get_file(**kwargs):

    db = Database()
    response = db.GetFile()
    return resp(**response)

#---------------------------------------------------------------
@rest_controller.route('/download/<path:filename>', methods=['GET','POST'])
def download_file(filename):
    '''url for download file'''

    try:
        return send_from_directory(app.static_folder,filename,as_attachment=True)

    except FileNotFoundError:
        return resp(404)


