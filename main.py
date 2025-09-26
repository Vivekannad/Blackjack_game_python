from chip import Chip
from hand import Hand
from deck import Deck

def divider(title=""):
    print("\n" + "=" * 40)
    if title:
        print(f"   {title}")
        print("=" * 40)

def take_bid(have_chips):
    while True:
        try:
            bid = int(input(f"\n💰 Chips Available: {have_chips.chips}\nEnter your bet: "))
        except ValueError:
            print("❌ Invalid input, enter a number")
        else:
            if bid <= 0:
                print("❌ Bet must be greater than 0")
            elif bid > have_chips.chips:
                print("❌ You don’t have enough chips")
            else:
                return bid

def hit_on_func(hand, new_deck):
    hand.add_cards(new_deck.deal_one())
    print(f"--> Card drawn: {hand.cards[-1]}")
    hand.handle_card()

def display_some(player, dealer):
    divider("Current Hands")
    print("Player's Hand:", ", ".join(str(c) for c in player.cards))
    print("Dealer's Hand:", dealer.cards[0], " + [hidden]")

def display_all(player, dealer):
    divider("Final Hands")
    print("Player's Hand:", ", ".join(str(c) for c in player.cards), f" | Total = {player.total}")
    print("Dealer's Hand:", ", ".join(str(c) for c in dealer.cards), f" | Total = {dealer.total}")

# Main Game
game_on = True
player_chip = Chip()

while game_on:
    round_over = False
    divider("New Round")
    player = Hand()
    dealer = Hand()

    bid = take_bid(player_chip)
    player_chip.bet_chip(bid)

    deck = Deck()
    deck.shuffle_cards()

    for _ in range(2):
        player.add_cards(deck.deal_one())
        dealer.add_cards(deck.deal_one())

    display_some(player, dealer)

    # Player's turn
    while True:
        choice = input("\n(H)it or (S)tand? ").strip().upper()
        if choice == "H":
            hit_on_func(player, deck)
            display_some(player, dealer)
            if player.check_if_bust():
                print(f"\n👎 Player BUSTED! Lost {bid}")
                round_over = True
                break
        elif choice == "S":
            print("\n-- Player stands --")
            break
        else:
            print("Please choose H or S")

    if not round_over:
        # Dealer's turn
        print("\n-- Dealer's Turn --")
        while dealer.total <= 16:
            hit_on_func(dealer, deck)
            if dealer.check_if_bust():
                print(f"\n🎉 Dealer BUSTED! Player wins {bid}")
                player_chip.win_chip()
                round_over = True
                break

        display_all(player, dealer)

        if not round_over:
            if dealer.total > player.total:
                print("\n Dealer Wins!")
            elif dealer.total < player.total:
                print(f"\n🎉 Player Wins {bid}!")
                player_chip.win_chip()
            else:
                player_chip.retain_chip();
                print("\n🤝 It's a DRAW!")

    print(f"\nChips Remaining: {player_chip.chips}")

    if player_chip.chips == 0:
        divider("Game Over")
        print("No chips left to continue.")
        break

    again = input("\nPlay another round? (y/n): ").strip().lower()
    if again != "y":
        game_on = False
