
class Player:
     def __init__(self, first_name="", last_name="", birth_date="", sex="", rank="") -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.name = self.first_name + " " + self.last_name

    def serialize(self):

        player = {}
        player['first_name'] = self.first_name
        player['last_name'] = self.last_name
        player['birth_date'] = self.birth_date
        player['sex'] = self.sex
        player['rank'] = self.rank
        player['name'] = self.first_name + " "+ self.last_name

        return player

    def save_player_to_DB(self)