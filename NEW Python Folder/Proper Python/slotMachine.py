import random


def spin():
    symbols = ["🍎", "🍌", "🍊", "🥭"]
    return [random.choice(symbols) for _ in range(3)]


def display(row):
    print(" | ".join(row))


def reward(bet, row):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍎":
            return bet * 2
        elif row[0] == "🍌":
            return bet * 3
        elif row[0] == "🍊":
            return bet * 4
        elif row[0] == "🥭":
            print("JACKPOT!")
            return bet * 5
    return 0


def main():
    Balance = 100
    print("Welcome To The Slot Machine")
    print("Symbols: 🍎 🍌 🍊 🥭")
    print(f"Current Balance: {Balance}")
    print("---------------------------")

    while Balance > 0:
        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Enter a valid number for your bet.")
            continue

        bet = int(bet)

        if bet > Balance or bet <= 0:
            print("Invalid bet amount! Check your balance or bet a positive amount.")
            continue

        row = spin()
        print("Spinning...\n")
        display(row)

        payout = reward(bet, row)
        Balance -= bet  # Deduct the bet first

        if payout > 0:
            print(f"You Won: {payout}!")
            Balance += payout  # Add the payout if won
        else:
            print("You Lost.")

        print(f"Current Balance: {Balance}\n")
        playAgain = input("Do you wish to play again (Y/N)").upper()

        if playAgain != "Y":
            break


    print("Game Over! You ran out of money.")


if __name__ == '__main__':
    main()
