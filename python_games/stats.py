class Gamestats:
    def __init__(self):
        self.game_active=False
        self.reset_score()
        self.high_score=0
    def reset_score(self):
        self.score=0
        self.level=1
        self.ship_limit=1