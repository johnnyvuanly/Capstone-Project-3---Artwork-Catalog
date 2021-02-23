from peewee import *
from model import Artist, Artwork

def add_artist():
    # add a new artist. ui.py gets user input for artist which connects to the model Artist that we grab
    Artist.get_or_create()

def search_artist_artwork(term):
    # search for all the artwork by an artist (everything - available and sold)
    query = Artwork.select().where((Artwork.artist).contains(term.lower()))
    return list(query)

def all_available_art():
    # display for all the available artwork by an artist
    available_art = Artwork.select().where(Artwork.available == True) & (Artwork.artist == artist)
    for artworks in available_art:
        return artworks

def add_artwork():
    # add a new artwork. Make sure the artwork is associated with an artist. If needed, create an artist first. 
    Artwork.get_or_create()

def delete_artwork():
    # delete an artwork
    query = Artwork.delete_instance(Artwork.artwork)


def change_availability():
    # change the availability status of an artwork, for example, change from available to sold
    change = Artwork.update({Artwork.available}).execute()