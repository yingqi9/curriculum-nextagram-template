from flask import Flask, Blueprint, sessions, render_template, request, redirect, url_for, flash, abort
from models.user import User
from werkzeug.security import check_password_hash

sessions_blueprint = Blueprint('sessions', __name__, template_folder='templates')

# Log in page
@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template("sessions/new.html")

@sessions_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    password_to_check = request.form['password']




