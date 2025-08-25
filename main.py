
from chip import Chip
from hand import Hand
from deck import Deck




def take_bid(have_chips):
    while True:
        try:
            bid = int(input("How much you wanna bid ? from 1 to {}" .format(have_chips.chips)))
        except ValueError:
            print("Not a number")
        else:
            if have_chips.chips < bid:
                print("Do not have that funds")
            else:
                break
    return bid

def hit_on_func(hand, new_deck):
    hand.add_cards(new_deck.deal_one())
    print("Card added of {} " .format(hand.cards[-1]))
    hand.handle_card()

def display_some(player, dealer):
    print("Player's Hand")
    for c in player.cards:
        print(c)

    print()
    print("Dealer card \n {}" .format(dealer.cards[0]))

def display_all(player , dealer):
    print("Player's Hand")
    for c in player.cards:
        print(c)

    print()
    print("Dealer card \n", *dealer.cards , sep="\n")

# def push(player , dealer):
#     if player.total == dealer.total:
#         return 0;
game_on = True
player_chip = Chip()
while game_on:
    round_over = False
    while game_on:
        print(game_on)
        player = Hand()
        dealer = Hand()
        bid = take_bid(player_chip)
        player_chip.bet_chip(bid)

        deck = Deck()
        deck.shuffle_cards()

        for i in range(2):
            player.add_cards(deck.deal_one())
            dealer.add_cards(deck.deal_one())

        display_some(player, dealer)
        choice = ""
        while choice.upper() != "S":
            choice = input("Press H for hit and S for stand")
            if choice.upper() == "H":
                hit_on_func(player , deck)
                display_some(player,dealer)
                if player.check_if_bust():
                    print(f"Player Busted and lost {bid}")
                    print("Dealer WON!!")
                    round_over = True
                    break
            elif choice.upper() == "S":
                print("Dealer's turn")
            else:
                print("Select from either of them")

        display_all(player, dealer)
        if  round_over:
            break
        while True:
            if dealer.total <= 16:
                print("As Dealer's hand is less than 17 , he will hit. ")
                hit_on_func(dealer , deck)
                display_all(player,dealer)
                if dealer.check_if_bust() :
                    print("Dealer Busted ")
                    print(f"Player Won ${bid}")
                    round_over = True
                    player_chip.win_chip()
                    break
            else:
                print("Dealer's hand is more than 17, he will stand")
                break

        print(f"Player total {player.total} and Dealer's total {dealer.total}")
        if not round_over:
            if dealer.total == player.total:
                print("It is a DRAW!!")
            elif dealer.total > player.total:
                print("Dealer WON!!!")
            else :
                print("Player WIN!!")
                player_chip.win_chip()
            break
        else:
            break

    if player_chip.chips == 0:
        print("No Chips To Proceed")
        game_on = False
        break

    choice = input("Do you want to go for another round? (y/n): ").strip().lower()
    if choice == "y":
        game_on = True
    else:
        game_on = False



