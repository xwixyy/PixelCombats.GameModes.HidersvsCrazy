class Game:
    def __init__(self):
        self.players = []
        self.madman = None

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            print(f"{player} добавлен в игру.")
        else:
            print(f"{player} уже в игре.")

    def block_madman_role(self, player):
        if self.madman == player:
            print(f"{player} не может снова стать безумцем.")
            return True
        return False

# Пример использования
game = Game()
game.add_player("Игрок1")
game.add_player("Игрок2")
game.madman = "Игрок1"
print(game.block_madman_role("Игрок1"))  # True
print(game.block_madman_role("Игрок2"))  # False