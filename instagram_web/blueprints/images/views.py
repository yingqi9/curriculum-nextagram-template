from flask import Blueprint, render_template, request, url_for, Flask, redirect, flash
from models.images import Images
from models.user import User
from config import Config
from flask_login import login_required, current_user
from werkzeug import secure_filename
from instagram_web.util.helpers import upload_file_to_s3


images_blueprint = Blueprint('images', 
                            __name__, 
                            template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html') 


#upload page
@images_blueprint.route('/new', methods=['POST'])
@login_required
def create():
    file = request.files["user_file"] #if no file in request
    if not file:
        flash("Please choose a photo.", "danger")
        return render_template('images/new.html')
    file.filename = secure_filename(file.filename)
    output = upload_file_to_s3(file) #import from helpers.py
    if not output: 
        flash("Unable to upload photo, try again.", "danger")
        return render_template('images/new.html')
    else:
        uploadphoto = Images(username=User.id, img_file=file)
        images = Images(username_id=current_user.id, img_file = output)
        print(output) 
        flash("Picture uploaded succesfully", "success")

    if images.save():
        flash("Done","success") 
        return redirect(url_for('images.new')) 
    else: 
        flash("Upload failed", "danger")
        return render_template('/images/new.html')

