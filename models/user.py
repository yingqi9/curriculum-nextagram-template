import peewee as pw
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash


class User(BaseModel):
    username = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField(unique=False)

    def save(self, *args, **kwargs):
    self.errors = []
    self.validate()

    if len(self.errors) == 0:
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)
    else:
        return 0

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