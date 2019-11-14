from flask import Blueprint, render_template, request, url_for, Flask, redirect, flash
from models.user import *
from config import S3_Bucket 
from flask_login import login_required, current_user



images_blueprint = Blueprint('images', 
                            __name__, 
                            template_folders='templates')


#upload page
@images_blueprint.route('/new', methods=['POST'])
@login_required

    