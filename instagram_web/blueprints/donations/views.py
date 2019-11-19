import braintree
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from config import Config
from models.donations import Donation

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
@login_required
def show(): 
    return render_template('donations/new.html')


@donations_blueprint.route('/paycheckout', methods=['POST'])
@login_required
def new(): 
    client_token = gateway.client_token.generate()

    return render_template('donations/new.html', client_token=client_token)


@donations_blueprint.route('/pay', methods=['POST'])
@login_required
def create():
    
    result = gateway.transaction.sale({
        "amount": "100.00",
        "payment_method_nonce": request.form["nonce"],
        "options": {
        "submit_for_settlement": True
        }
    })

    if result.is_success:
        flash("Successfully donated!", "success")
        return redirect(url_for('images.new'))
    
    else:
        flash("Transaction error has occured, please try again.", "danger")
        return render_template('donations/new.html')