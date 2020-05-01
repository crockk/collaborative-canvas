from database import db
from database import User

def create():
    db.create_tables([User])
