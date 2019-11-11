from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for, session
from models.user import User
from werkzeug.security import check_password_hash


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
    password = request.form.get('password')
    user = User.get_or_none(username=username)
    if user: #if have user 
        result = check_password_hash(user.password, reuqest.form.get('password'))
        print(result)
        if result: 
            session["user_id"] = user.id
            flash('Succesfully log in!')
            return redirect (url_for('sessions/new')
        else: 
            flash('Incorrect password.')
            return render_template('/sessions/new.html') 

    else: #if no user
        flash('No user found')
        return render_template('/sessions/new.html') 

@sessions_blueprint.route('/logout', methods=['GET'])
def destroy():
    session.pop('username', None)
    flash('Successfully logged out.', 'success') 
    return render_template('sessions/new.html') 
