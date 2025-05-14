class ATM:
    def __init__(self):
        """
        Initialize ATM with a default balance and PIN.
        """
        self.balance = 40000
        self.pin = '4347'
        self.pin_verified = False

    def check_pin(self, input_pin):
        """
        
        Check if the entered PIN is correct.
        """
        if input_pin == self.pin:
            self.pin_verified = True
            print("PIN verified successfully.")
            return True
        else:
            self.pin_verified = False
            print("Incorrect PIN. Access denied.")
            return False

    def check_balance(self):
        """
        Print the current balance.
        """
        print(f"Your current balance is: Rs. {self.balance}")

    def deposit(self, amount):
        """
        Deposit the given amount if PIN is verified and amount is valid.
        """
        if not self.pin_verified:
            print("Please enter the correct PIN before depositing.")
            return
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        self.balance += amount
        print(f"Rs. {amount} deposited successfully.")
        self.check_balance()

    def withdraw(self, amount):
        """
        Withdraw the given amount if PIN is verified, amount is valid, and balance is sufficient.
        """
        if not self.pin_verified:
            print("Please enter the correct PIN before withdrawing.")
            return
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Rs. {amount} withdrawn successfully.")
        self.check_balance()

    def exit(self):
        """
        Exit the ATM program.
        """
        print("Thank you for using the ATM. Goodbye!")


def main():
    atm = ATM()
    print("Welcome to ATM")
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        input_pin = input("Enter your PIN: ")
        if atm.check_pin(input_pin):
            break
        attempts += 1
        if attempts == max_attempts:
            print("Too many incorrect attempts. Exiting.")
            return
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '4':
            atm.exit()
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()