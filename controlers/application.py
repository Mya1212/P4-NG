from views.menu import menu_views

class menu_controller:

    def __init__(self):
        self.menu=menu_views()

    def main_menu(self):
        self.menu_views.display_main_menu()
        user_input=input

        if user_input=="1":
        
        elif user_input=="2":

        elif user_input=="3":

        else :
            print("error")

        