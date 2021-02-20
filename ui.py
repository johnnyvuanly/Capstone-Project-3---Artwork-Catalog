from model import Artist, Artwork
from menu import Menu

def display_menu_get_choice(menu):
    """ Display all of the menu options, checks that the user enters a valid choice and returns the choice.
    :param menu: the menu to display
    :returns: the user's choice ie number they input """
    while True:
        print(menu)
        choice = input('Enter an option: ')
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')


def get_artist_info():
    """ Create a new Artist from name and email provided by user
    :returns: a Artist created from the name and email. """
    name = input('Enter artist\'s name: ')
    email = input('Enter their email: ')
    return Artist(name=name, email=email)