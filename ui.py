from model import Artist, Artwork

def get_artist_info():
    """ Create a new Artist from name and email provided by user
    :returns: a Artist created from the name and email. """
    name = input('Enter artist\'s name: ')
    email = input('Enter their email: ')
    return Artist(name=name, email=email)