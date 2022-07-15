from controlers.player import Player

class CreatePlayer:

    first_name = input('Entrez votre nom :\n>')
    last_name = input('Entrez votre prénom :\n>')
    birthday = input ('Entrez votre date de naissance XX/XX/XXXX:\n>')
    sex = input ('Entrez votre genre F ou M:\n>')
    rank = input ('Entrez votre classement:\n>')

    def ask_gender(self) -> str:
        if sex == "F" or sex == "M":
            return sex
        else:
            print("Erreur veuillez entrez un genre valide F ou M")