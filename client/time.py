import time

class Timer:
    def __init__(self, minutes):
        self.minutes = minutes

    def start_timer(self):
        print(f"Таймер на {self.minutes} минут(ы) запущен.")
        time.sleep(self.minutes * 60)
        print("Время вышло!")

# Пример использования
timer = Timer(10)
timer.start_timer()