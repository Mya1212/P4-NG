from controlers.application import application_controller

def main():
    app=application_controller()
    app.run()

if __name__ == "__main__":
    main()




"""
    def serialize(self):
        Return a dictionnary from the objects attributs
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            # 'birthday': self.birthday.strftime('%Y-%m-%d'),
            "sex": self.sex,
            "rank": self.rank,
        }
        return serialized_player
"""