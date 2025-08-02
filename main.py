import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols_count):
    all_symbols = []
    for symbol, count in symbols_count.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], end=" | ")
        print()

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("Invalid input.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines (1 to {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
        print("Invalid input.")

def get_bet():
    while True:
        amount = input(f"Enter your bet (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
        print("Invalid input.")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        print(f"Not enough balance. You have ${balance}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_count)
    print(f"You won ${winnings}")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    else:
        print("No winning lines.")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press Enter to play (q to quit): ")
        if answer.lower() == 'q':
            break
        balance += spin(balance)
        if balance <= 0:
            print("You have no money left. Game Over!")
            break
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
