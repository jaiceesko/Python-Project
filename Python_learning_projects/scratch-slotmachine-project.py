# the deposit the user is entering
# as well as their bet

# we define a function for the deposit

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10 

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please, Amount must be greater than 0!")
        else:
            print("Please enter a valid amount!")
    return amount  


# we define a function for the betting

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please, Enter a valid number of line(s)!")
        else:
            print("Please enter a valid number.")
            
    return lines
      
      
def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please, Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
            
    return bet



def main():
    balance = deposit()
    lines = get_number_of_lines()
    betting = get_bet()
    total_bet = betting  * lines
    if lines == 1:
        print(f"${balance}, you are betting on {lines} line. Total bet is equal to: ${total_bet}")
    else:
        print(f"${balance}, you are betting on {lines} lines. Total bet is equal to: ${total_bet}")

main()