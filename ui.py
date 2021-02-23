from model import Artist, Artwork

def get_artist_info():
    """ Create a new Artist from name and email provided by user
    :returns: a Artist created from the name and email. """
    name = input('Enter artist\'s name: ')
    email = input('Enter their email: ')
    return Artist(name=name, email=email)

def get_artists_artwork():
    while True:
        try:
            artist_name = input('Which artist\'s artwork work do you want to see? ')
            artwork_name = input('What is the name of the art piece you wish to see? ')
            if artist_name.length() and artwork_name.length() > 0: 
                return Artwork(artwork_name)
            else: 
                print(f'Could not find an art piece with the name of {artwork_name} by {artist_name}.')

        except EOFError:
            print('Please enter the artist name and artwork name.')

def display_all_artwork(artworks):
    if artworks:
        for artwork in artworks:
            print(artwork)
    else:
        print('No artwork to display')

def get_availability_status():
    while True:
        response = input('Enter \'is\' if the artwork is available or \'is not\' if the artwork is not available: ')
        if response.lower() in ['is', 'is not']:
            return response.lower() == 'is'
        else:
            print('Type \'is\' or \'is not\'')

