from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField
from flask_login import UserMixin

db = SqliteDatabase('pixr.sqlite')
db.connect()


class User(UserMixin, Model):
    """ Peewee model for Abstract Unit """
    username = CharField(unique=True)
    password = CharField()

    def __str__(self): return self.username

    class Meta:
        database = db


class Cards(Model):
    """ Peewee model for Hero Unit """
    card_name = CharField(unique=True)
    rarity_value = CharField()

    class Meta:
        database = db

    def __str__(self): return self.card_name

if __name__ == "__main__":
    db.drop_tables([User, Cards])
    db.create_tables([User, Cards])
    user = User.create(username='test', password='password')

