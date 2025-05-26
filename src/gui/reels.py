import random

class Reel:
    SYMBOLS = ['🍒', '🍋', '🍊', '🍇', '🔔', '7']

    @staticmethod
    def weighted_choice(probabilities):
        # probabilities: dict of symbol -> percent
        symbols = list(probabilities.keys())
        weights = list(probabilities.values())
        return random.choices(symbols, weights=weights, k=1)[0]

    def __init__(self):
        self.current_symbol = None

    def spin(self, probabilities=None):
        if probabilities:
            self.current_symbol = Reel.weighted_choice(probabilities)
        else:
            self.current_symbol = random.choice(Reel.SYMBOLS)

    def get_symbol(self):
        return self.current_symbol