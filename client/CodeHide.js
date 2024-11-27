import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.is_hiding = False

class Game:
    def __init__(self):
        self.players = []
        self.hider_countdown = 20
        self.crazy_player = None

    def add_player(self, player_name):
        player = Player(player_name)
        self.players.append(player)

    def start_game(self):
        print("Игра началась! У вас есть 20 секунд, чтобы спрятаться!")
        self.hide_phase()

    def hide_phase(self):
        for i in range(self.hider_countdown, 0, -1):
            print(f"{i} секунд осталось, чтобы спрятаться...")
            time.sleep(1)

        self.choose_crazy_player()
        self.start_hunt()

    def choose_crazy_player(self):
        self.crazy_player = random.choice(self.players)
        print(f"БЕЗУМЕЦ выбрался! Это {self.crazy_player.name} с ножом!")

    def start_hunt(self):
        print("Начинается охота!")
        # Здесь можно добавить логику для нахождения игроков
        # Например, просто выводим всех игроков
        for player in self.players:
            if player != self.crazy_player:
                print(f"{player.name} прячется...")
            else:
                print(f"{player.name} ищет!")

# Пример использования
if __name__ == "__main__":
    game = Game()
    game.add_player("Игрок1")
    game.add_player("Игрок2")
    game.add_player("Игрок3")

    game.start_game()