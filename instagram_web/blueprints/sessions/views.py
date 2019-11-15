from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for, session
from instagram_web.util.google_oauth import oauth
from flask_login import login_user, logout_user, current_user
from models.user import User
from werkzeug.security import check_password_hash

sessions_blueprint = Blueprint('sessions',
                                __name__, 
                                template_folder='templates')

# log in page
@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/new.html')

@sessions_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    user = User.get_or_none(username=username) 
#if have user 
    if user: 
        result = check_password_hash(user.password, request.form.get('password'))

        if result: 
            # session["user_id"] = user.id
            login_user(user)
            flash('Succesfully log in!')
            return redirect (url_for('users.edit', id=current_user))
        else: 
            flash('Incorrect password.')
            return render_template('sessions/new.html')

#if no user
    else: 
        flash('User not found')
        return render_template('/sessions/new.html') 


@sessions_blueprint.route('/login/google', methods=['GET'])
def google_login():
    redirect_uri = url_for('sessions.authorize_google', _external=True) 
    return oauth.google.authorize_redirect(redirect_uri)


@sessions_blueprint.route('/authorize/google', methods=['GET'])
def authorize_google():
    token = oauth.google.authorize_access_token()
    if not token:
        flash('Opps, something went wrong, try again!', 'danger')
        return redirect(url_for('home'))
    
    email = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()['email']
    
    user = User.get_or_none(User.email == email)

    if not user: 
        flash('Sorry, no account register with this email', 'danger')
        return redirect(url_for('home'))

    flash('Welcome back!', 'success')
    login_user(user)
    return redirect(url_for('home'))


@sessions_blueprint.route('/logout', methods=['GET'])
def destroy():
    # session.pop('user_id', None)
    logout_user()
    flash('Successfully logged out.', 'success') 
    return redirect(url_for('sessions.new')) 