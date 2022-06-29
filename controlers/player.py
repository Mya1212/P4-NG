#appeler views player

#creer methode créer joueur

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


"""
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value != "M" and value != "F":
            raise ValueError("Le sex doit etre F ou M")
        self._sex = value

    @property
    def full_name(self):
        return self.first_name + " " + self.name
@FGLnK+4ae4JVtkf

    """

if __name__ == "__main__":
    player = Player("pierre","dupont","12-12-1988","M","800")
    print(player)
    data = player.serialize()
    print(data)