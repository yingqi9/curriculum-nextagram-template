import os
import peewee as pw
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from config import Config
from playhouse.hybrid import hybrid_property


class User(UserMixin,BaseModel):
    username = pw.CharField(unique=True)
    password = pw.CharField()
    email = pw.CharField(unique=True)
    profile_image_url = pw.TextField(null=True)

    @hybrid_property
    def profile_picture(self):
        if self.profile_image_url: # if the user has a profile image, it will display the profile pic, 
            return Config.S3_LOCATION + self.profile_image_url
        else:
            return "null" # else, it will return as nothing.
            

    def is_authenticated():
        return True


    def validate(self):
        duplicate_name = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_name:
            self.errors.append('Registraion failed. Username has already been taken!') 
        if duplicate_email:
            self.errors.append('Email address already in used!')
        # if len(self.password) < 8:
        #     self.errors.append('Password must not less than 8 characters')
        # if len(self.password) > 8:
        #     self.errors.append('Password must more than 25 characters') 
        # else: 
        #     self.password=generate_password_hash(self.password)
