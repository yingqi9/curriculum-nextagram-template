from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user

followers_blueprint = Blueprint('followers', 
                                __name__, 
                                template_folder='templates')


@followers_blueprint.route()
