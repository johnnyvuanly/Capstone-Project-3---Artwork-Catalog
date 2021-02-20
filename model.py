from peewee import *
from config import db_path

db = SqliteDatabase(db_path)

# Create Model class which defines both the fields in the objects in your program
# and also the columns in the database. PeeWee maps between the two.
class Artist(Model):
    """ Represents an artist in the database """
    name = CharField()
    email = CharField()

    # Link this model to a particular database
    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is the artists name and their email is {self.email}.'

# Connect to DB, and create tables that map to the model Artist.
# Can have many models, create_tables takes a list of model classes as an arguement
db.connect()
db.create_tables([Artist])

class Artwork(Model):
    """ Represents Artwork in the database """
    artist = ForeignKeyField(Artist, backref='artists')
    artwork = CharField()
    price = FloatField()
    available = BooleanField(default=True)

    class Meta:
        database = db
    
    def __str__(self):
        available_status = 'is' if self.available else 'is not'
        return f'The artwork is named {self.artwork} and the artist who made it is named {self.artist}. It is priced at {self.price} and {available_status} available.'

db.create_tables([Artwork])