from datetime import datetime


class Clock:
    def __init__(self):
        self.start_time = []
        self.final_time = []

    def start(self):
        self.start_time = datetime.now().strftime("%X").split(":")

    def end_and_get_final_time(self):
        self.final_time = datetime.now().strftime("%X").split(":")
        minutes_of_the_game = int(self.final_time[1]) - int(self.start_time[1])
        seconds_of_the_game = int(self.final_time[2]) - int(self.start_time[2])
        if seconds_of_the_game < 0:
            minutes_of_the_game -= 1
            seconds_of_the_game = 60 - abs(seconds_of_the_game)
        if seconds_of_the_game < 10:
            seconds_of_the_game = f"0{seconds_of_the_game}"
        return f"{minutes_of_the_game}:{seconds_of_the_game}"
