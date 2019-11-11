import peewee as pw
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash


class User(BaseModel):
    username = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField(unique=False)

    def validate(self):
        duplicate_name = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_name:
            self.errors.append('Registraion failed. Username has already been taken!')

        if duplicate_email:
            self.errors.append('Email address already in used!')
