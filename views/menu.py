class Menu_views:

    def __init__(self):
        pass

#rajouter input joueur, boucle verif input correct, return choix
    def display_main_menu(self):
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Tournament menu")
        print("[2] Player menu")
        print("[3] Exit program")

    def display_tournament_menu(self):
        print("\n\n=== TOURNAMENT MENU ===\n")
        print("[1] Tournament list")
        print("[2] Create tournanment")
        print("[3] Return main menu")

    def display_player_menu(self):
        print("\n\n=== PLAYER MENU ===\n")
        print("[1] Players list")
        print("[2] Create player")
        print("[3] Return main menu")

    def error_input(self):
        print("error")


