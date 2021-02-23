import peewee
from model import Artwork, Artist
import db
import ui

def main():
   ui.print_menu()

   user_input = 0

   while user_input != 7:
       user_input = input('Enter Choice: ')


