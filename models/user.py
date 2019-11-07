from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    uername = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField(unique=False)