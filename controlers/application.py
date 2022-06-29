from views.menu import menu_views
from sys import exit
from tinydb import TinyDB

class ApplicationController:

    def __init__(self):
        self.menu=menu_views()

# rajouter boucle while
    def main_menu(self):
        self.menu_views.display_main_menu()
        user_input=input()

        if user_input=="1":
            self.menu_views.display_tournament_menu()
        
        elif user_input=="2":
            self.menu_views.display_player_menu()

        elif user_input=="3":

        else :
            print("error")

        