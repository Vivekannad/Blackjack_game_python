# BlackJack Game

A simple console-based Blackjack game written in Python.
This game follows the traditional Blackjack rules where you play against the dealer. You start with 20 chips and can place bets each round. The goal is to beat the dealer without going over 21

## 📌 Features
- Classic Blackjack rules (player vs dealer).

- Chip system: start with 20 chips and place bets each round.

- Ace handling: Ace counts as 11, but switches to 1 if your total exceeds 21.

- Dealer automatically hits until 17 or higher.

- Player can Hit (H) or Stand (S).

- Win, Lose, or Draw messages displayed at the end of each round.

- Multiple rounds until chips run out.

## How to Run
1. Clone the repository
2. Make sure You have Python 3.0 installed.
3. Run the game from terminal.
    ```
        python main.py
   ```
   
## Gameplay Instructions
1. The game starts with 20 chips.
2. You will be asked how much you want to bet.
3. Cards are dealt:
- Player gets 2 cards.
- Dealer gets 2 cards (one hidden).
4. Player's turn:
- Press H to Hit (take another card).
- Press S to Stand (end your turn).

5. If your total exceeds 21, you bust and lose the round.

6. Dealer's turn:

- Dealer must Hit until reaching at least 17.

- If dealer busts, you win.

7. Compare hands:

- Higher hand wins (without going over 21).

- Equal totals = Draw.

8. Win doubles your bet. Lose deducts your bet.

9. Play continues until you run out of chips or quit.

## Developer
Made with love by **Vivek Anand**.