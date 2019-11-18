import braintree
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from config import Config
# from models.donations import Donations



donations_blueprint = Blueprint('donations', 
                                __name__, 
                                template_folder='templates')

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=Config.BT_MERCHANT_ID,
        public_key=Config.BT_PUBLIC_KEY,
        private_key=Config.BT_PRIVATE_KEY
    )
)

@donations_blueprint.route('/pay', methods=['GET'])
def show(): 
    return render_template('donations/new.html')


@donations_blueprint.route('/paycheckout', methods=['POST'])
def new(): 
    client_token = gateway.client_token.generate()

    return render_template('donations/new.html', client_token=client_token)