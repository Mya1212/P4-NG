from views.player import PlayerViews
from views.menu import MenuViews

class Player:
    def __init__(self, first_name, last_name, birth_date, sex, rank) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name

    def serialize(self):

        data_player = {}
        data_player['first_name'] = self.first_name
        data_player['last_name'] = self.last_name
        data_player['birth_date'] = self.birth_date
        data_player['sex'] = self.sex
        data_player['rank'] = self.rank
        data_player['name'] = self.first_name + " "+ self.last_name

        return data_player

    def save_player_to_DB(self):
        """ save the player to the database """

    def create_player(self):
        self.views.CreatePlayer()

    def update_player(self):
        while True:
            self.menu.display_player_menu()
            user_input=input()

            if user_input=="1":
                #player list
                #select player
                #edit
                pass
            
            elif user_input=="2":
                #player list
                #select player
                #delete
                pass

            elif user_input=="3":
                self.menu.display_player_menu()
            
            else:
                self.menu.display_message("Invalid choice")

    def display_player_name(self):
        #players = []
        #players.sort(key=)
        self.views.diplay_player_list()

    def display_player_rank(self, sort_by: str):
        self.views.diplay_player_list()
        
    def menu_player(self):
        while True:
            self.menu.display_player_menu()
            user_input=input()

            if user_input=="1":
                self.create_player()
            
            elif user_input=="2":
                self.update_player()

            elif user_input=="3":
                self.display_player_name()

            elif user_input=="4":
                self.display_player_rank()

            elif user_input=="5":
                self.menu.display_player_menu()
                exit()
            
            else:
                self.menu.display_message("Invalid choice")

if __name__ == "__main__":
    player = Player("pierre","dupont","12-12-1988","M","800")
    print(player)
    data = player.serialize()
    print(data)