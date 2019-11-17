import braintree
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from models.donations import Donations 



donations_blueprint = Blueprint('donations', 
                                __name__, 
                                template_folder='templates')

@donations_blueprint.route()


