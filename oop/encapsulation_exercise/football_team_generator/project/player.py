class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        result = f"Player: {self.__name}\n"
        result += f"Sprint: {self.__sprint}\n"
        result += f"Dribble {self.__dribble}\n"
        result += f"Passing: {self.__passing}\n"
        result += f"Shooting: {self.__shooting}"


player = Player("A", 20, 30, 40, 50)
print(player.__str__())