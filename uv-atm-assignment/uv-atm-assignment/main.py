class ATM:
    def __init__(self):
        # Initial balance and default PIN
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: Rs.{self.balance}")

    def deposit(self, amount, input_pin):
        if not self.check_pin(input_pin):
            print("❌ Wrong PIN. Deposit canceled.")
            return
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"✅ Deposited Rs.{amount}. New balance: Rs.{self.balance}")

    def withdraw(self, amount, input_pin):
        if not self.check_pin(input_pin):
            print("❌ Wrong PIN. Withdrawal canceled.")
            return
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
            return
        self.balance -= amount
        print(f"✅ Withdrew Rs.{amount}. New balance: Rs.{self.balance}")

    def exit(self):
        print("Thank you for using our ATM. Goodbye!")


# --- Interactive loop. ---
def run_atm():
    atm = ATM()
    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            pin = int(input("Enter your PIN: "))
            if atm.check_pin(pin):
                atm.check_balance()
            else:
                print("❌ Wrong PIN.")
        elif choice == '2':
            pin = int(input("Enter your PIN: "))
            amt = float(input("Enter amount to deposit: Rs"))
            atm.deposit(amt, pin)
        elif choice == '3':
            pin = int(input("Enter your PIN: "))
            amt = float(input("Enter amount to withdraw: Rs"))
            atm.withdraw(amt, pin)
        elif choice == '4':
            atm.exit()
            break
        else:
            print("❌ Invalid selection. Please choose 1-4.")

if __name__ == '__main__':
    run_atm()