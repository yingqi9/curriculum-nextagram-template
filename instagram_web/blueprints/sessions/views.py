from flask import Blueprint, Flask, abort, flash, redirect, render_template, request, url_for, session
from models.user import User
from from werkzeug.security import check_password_hash


sessions_blueprint = Blueprint('sessions',
                                __name__, 
                                template_folder='templates')

#log in page
@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/new.html')

@sessions_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    password_to_check = request.form['password']
    hashed_password = user.hashed_password
    


@sessions_blueprint.route('/delete', methods=['GET'])
def delete():
     flash('Successfully logged out')
     return render_template('sessions/new.html')
