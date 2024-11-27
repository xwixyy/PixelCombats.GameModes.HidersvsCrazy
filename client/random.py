import random

class Game:
    def __init__(self, players):
        self.players = players
    
    def randomize_madman(self):
        if len(self.players) == 0:
            return None
        madman = random.choice(self.players)
        print(f"Безумец выбран: {madman}")
        return madman

# Пример использования
players_list = ["Игрок1", "Игрок2", "Игрок3", "Игрок4"]
game = Game(players_list)
madman = game.randomize_madman()