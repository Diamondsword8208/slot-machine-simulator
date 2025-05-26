from gui.reels import Reel

class SlotMachine:
    def __init__(self):
        self.reels = [Reel(), Reel(), Reel()]

    def spin_reels(self):
        for reel in self.reels:
            reel.spin()

    def get_results(self):
        return [reel.get_symbol() for reel in self.reels]