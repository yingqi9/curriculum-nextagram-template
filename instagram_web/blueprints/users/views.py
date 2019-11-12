from flask import Blueprint, render_template, request, url_for, Flask, redirect, flash
from models.user import *
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

#users/new
@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')

#users/sign up page
@users_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = generate_password_hash(password)
    formsign = User(username=username, email=email, password=hashed_password)
    if formsign.save():
        flash('Succesfully sign up!') 
        return redirect(url_for('users.new')) 
    else: 
        flash('Registration failed. Username has been taken!!')
        return render_template('/users/new.html',errors=formsign.errors)

    # formsign.save()
    
    # return redirect(url_for('users.new'))

@users_blueprint.route('/', methods=["GET"]) 
def index():
    return "USERS"


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/<id>/edit', methods=['GET']) #edit profile 
@login_required
def edit(id):
    user = User.get_by_id(id)
    print(user.username)
    if current_user == user:
        return render_template("users/edit.html", user=user)
    else:
        flash(f"You are not allowed to update {user.username} profile", "danger")
        return render_template("users/show.html", user=current_user)

@users_blueprint.route('/<id>', methods=['POST']) #update profile
@login_required
def update(id):
    user = user.get_by_id(id)
    if current_user == user:
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.password = request.form.get('password')
        if user.save():
            flash("Succesfully update", "success")
            return redirect(url_for('users.edit', id=id))
        else:
            flash("Cannot update profile", "danger")
            return render_template("users/edit.html", user=user)
    else:
        flash(f"You are not allowed to update {user.name} profile", "danger")
        return render_template("users/edit.html", user=user)
            
