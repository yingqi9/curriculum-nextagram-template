import os
import peewee as pw
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash
from models.user import User


class Images(BaseModel):
    username = pw.ForeignKeyField(User, backref="Images")
    img_file = pw.CharField(null=True)


