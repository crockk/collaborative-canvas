from database import db
from database import User

def drop():
    db.drop_tables([User])
