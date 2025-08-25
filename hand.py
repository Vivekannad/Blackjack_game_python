class Hand:

    def __init__(self):
        self.cards = []
        self.total = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.total += card.value

    def handle_card(self):
        if self.total > 21:
            for card in self.cards:
                if card.rank == "Ace":
                    card.value = 1
                    self.total -= 10

    def check_if_bust(self):
        if self.total > 21:
            return True  # means bust
        else:
            return False # means not bust