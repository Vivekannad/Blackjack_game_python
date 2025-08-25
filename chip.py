class Chip:

    def __init__(self):
        self.chips = 20
        self.bet_chips = 0

    def bet_chip(self, chip):
        if chip > self.chips:
            self.chips -= self.chips
            self.bet_chips = self.chips
        else:
            self.chips -= chip
            self.bet_chips = self.chips

    def win_chip(self):
        self.chips += (self.bet_chips * 2)

    def __str__(self):
        return f"You have {self.chips} chips"

