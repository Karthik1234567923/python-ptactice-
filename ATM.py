# ATM Simulation Project (Final Version)

print("Welcome to ATM System")

pin = 1234

# Load balance from file
try:
    file = open("balance.txt", "r")
    balance = int(file.read())
    file.close()
except:
    balance = 15000  # default balance


# Function: Save balance to file
def save_balance(balance):
    file = open("balance.txt", "w")
    file.write(str(balance))
    file.close()


# Function: Balance Inquiry
def show_balance(balance):
    print("Your balance is:", balance)


# Function: Deposit
def deposit(balance):
    try:
        amount = int(input("Enter deposit amount: "))
    except:
        print("Invalid input!")
        return balance

    if amount <= 0:
        print("Invalid deposit amount")
        return balance

    balance += amount
    print("Deposit successful")
    print("Updated balance:", balance)

    save_balance(balance)   # save to file
    return balance


# Function: Withdraw (WITH LIMIT)
def withdraw(balance):
    try:
        amount = int(input("Enter withdrawal amount: "))
    except:
        print("Invalid input!")
        return balance

    if amount > 50000:
        print("Withdrawal limit is 50000")
        return balance

    if amount <= balance:
        balance -= amount
        print("Withdraw successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

    save_balance(balance)   # save to file
    return balance


# PIN Verification
pin_input = input("Enter your PIN: ")

if not pin_input.isdigit():
    print("Invalid PIN input")
    exit()

entered_pin = int(pin_input)

# Main Program
if entered_pin == pin:

    while True:
        print("\n------ ATM MENU ------")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            show_balance(balance)
            input("Press Enter to go back to menu...")

        elif choice == 2:
            balance = withdraw(balance)
            input("Press Enter to go back to menu...")

        elif choice == 3:
            balance = deposit(balance)
            input("Press Enter to go back to menu...")

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")
