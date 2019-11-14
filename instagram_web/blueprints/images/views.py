from flask import Blueprint, render_template, request, url_for, Flask, redirect, flash
from models.user import *
from config import Config
from flask_login import login_required, current_user



images_blueprint = Blueprint('images', 
                            __name__, 
                            template_folder='templates')


# #upload page
# @images_blueprint.route('/new', methods=['POST'])
# @login_required
# def create():
#     file = request.files["user_file"] #if no file in request
#     if not file:
#         flash("Please choose a file.", "danger")
#         return render_template('images/new.html')
#     file.filename = secure_filename(file.filename)
#     output = upload_file_to_s3(file) #import from helpers.py
#     if not output: 
#         flash("Unable to upload file, try again.", "danger")
#         return render_template('images/new/html')
    # else:
#         user = User.update(profile_image_url = output).where(User.id == current_user.id)
#         user.execute()
#         print(output)
#         flash("Profile picture updated", "success")
    
#         return redirect(url_for('users.edit',id=id)) 
    