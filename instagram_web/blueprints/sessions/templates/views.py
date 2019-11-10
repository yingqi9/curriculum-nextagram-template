from flask import Flask, sessions, Blueprint, render_template, request, redirect, url_for
from models.user import *
from werkzeug.security import check_password_hash

sessions_blueprint = Blueprint('sessions', __name__, template_folder='templates')

# Log in page
@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template("sessions/new.html")
