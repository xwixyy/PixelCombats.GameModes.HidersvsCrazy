import random
import time
import threading

class Player:
    def __init__(self, name):
        self.name = name
        self.role = None
        self.has_knife = False

    def assign_role(self, role):
        self.role = role
        print(f"{self.name} получил роль: {role}")

    def give_knife(self):
        self.has_knife = True
        print(f"{self.name} получил нож!")

class Game:
    def __init__(self):
        self.players = []
        self.madman = None

    def add_player(self, player_name):
        player = Player(player_name)
        self.players.append(player)
        print(f"{player_name} добавлен в игру.")

    def randomize_madman(self):
        if len(self.players) == 0:
            print("Нет игроков для выбора.")
            return None
        self.madman = random.choice(self.players)
        self.madman.assign_role("Безумец")
        print(f"Безумец выбран: {self.madman.name}")
        return self.madman

    def start_timer(self):
        print("Таймер на 20 секунд запущен.")
        time.sleep(20)
        self.give_knives_to_players()

    def give_knives_to_players(self):
        for player in self.players:
            player.give_knife()

    def start_game(self):
        madman = self.randomize_madman()
        timer_thread = threading.Thread(target=self.start_timer)
        timer_thread.start()

# Пример использования
if __name__ == "__main__":
    game = Game()
    game.add_player("Игрок1")
    game.add_player("Игрок2")
    game.add_player("Игрок3")
    
    game.start_game()