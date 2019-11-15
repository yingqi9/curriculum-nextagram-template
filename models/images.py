import os
import peewee as pw
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash
from models.user import User
from playhouse.hybrid import hybrid_property
from config import Config 


class Images(BaseModel):
    username = pw.ForeignKeyField(User, backref="images")
    img_file = pw.CharField(null=True)

    @hybrid_property
    def profile_image_url(self):
      return Config.S3_LOCATION + self.img_file