class Score:
    def __init__(self):
        self.score = 0

    def restart(self):
        self.score = 0

    def up(self):
        self.score += 1

    def get(self):
        return self.score
