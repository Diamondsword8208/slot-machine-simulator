class PayoutCalculator:
    def __init__(self):
        self.payouts = {
            'cherry': 2,
            'lemon': 3,
            'orange': 4,
            'plum': 5,
            'bell': 10,
            'seven': 20
        }

    def calculate_payout(self, symbols):
        if not symbols:
            return 0
        
        unique_symbols = set(symbols)
        payout = 0
        
        if len(unique_symbols) == 1:
            symbol = unique_symbols.pop()
            payout = self.payouts.get(symbol, 0)
        
        return payout