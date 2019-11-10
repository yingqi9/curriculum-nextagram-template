from flask import Blueprint, render_template, request, url_for, Flask, redirect, flash
from models.user import *
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
        # flash('Registration failed. Username has been taken!!')
        return render_template('/users/new.html',errors=formsign.errors)

    # formsign.save()
    
    # return redirect(url_for('users.new'))

@users_blueprint.route('/', methods=["GET"]) 
def index():
    return "USERS"


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
