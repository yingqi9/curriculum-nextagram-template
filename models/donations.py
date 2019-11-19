import peewee as pw
from models.base_model import BaseModel
from models.user import User
from models.images import Images

class Donation(BaseModel):
    username = pw.ForeignKeyField(User)
    images = pw.ForeignKeyField(Images)
    donation = pw.DecimalField()