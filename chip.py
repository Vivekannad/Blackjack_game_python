class Chip:

    def __init__(self):
        self.chips = 20
        self.bet_chips = 0

    def bet_chip(self, chip):
        if chip > self.chips:
            raise ValueError("Not enough chips to place this bet")
        self.chips -= chip
        self.bet_chips = chip

    def win_chip(self):
        self.chips += (self.bet_chips * 2)
        self.bet_chips = 0

    def retain_chip(self):
        self.chips += self.bet_chips

    def __str__(self):
        return f"You have {self.chips} chips"

