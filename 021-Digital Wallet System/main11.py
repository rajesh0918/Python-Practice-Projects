class Digital_Wallet:

    def __init__(self, owner_name, wallet_id, balance):
        self.owner_name = owner_name
        self.wallet_id = wallet_id
        self.balance = balance

    # Add money
    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print("Money added successfully!")
        else:
            print("Invalid amount.")

    # Make payment
    def make_payment(self, amount):
        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Payment successful!")

    # Check balance
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Display wallet details
    def display(self):
        print("\n===== WALLET DETAILS =====")
        print("Owner Name:", self.owner_name)
        print("Wallet ID:", self.wallet_id)
        print("Balance:", self.balance)


# Store all wallet objects
wallets = []


# Find wallet using wallet ID
def find_wallet(wallet_id):

    for wallet in wallets:
        if wallet.wallet_id == wallet_id:
            return wallet

    return None


# Create wallet
def create_wallet():

    owner_name = input("Enter your name: ")
    wallet_id = int(input("Enter wallet ID: "))

    # Check duplicate wallet ID
    if find_wallet(wallet_id) is not None:
        print("Wallet ID already exists.")
        return

    balance = float(input("Enter starting balance: "))

    if balance < 0:
        print("Balance cannot be negative.")
        return

    wallet = Digital_Wallet(owner_name, wallet_id, balance)

    wallets.append(wallet)

    print("Wallet created successfully!")


# View wallet
def view_wallet():

    wallet_id = int(input("Enter wallet ID: "))

    wallet = find_wallet(wallet_id)

    if wallet is not None:
        wallet.display()
    else:
        print("Wallet not found.")


# Add money
def add_money():

    wallet_id = int(input("Enter wallet ID: "))

    wallet = find_wallet(wallet_id)

    if wallet is not None:
        amount = float(input("Enter amount to add: "))

        wallet.add_money(amount)

    else:
        print("Wallet not found.")


# Make payment
def make_payment():

    wallet_id = int(input("Enter wallet ID: "))

    wallet = find_wallet(wallet_id)

    if wallet is not None:
        amount = float(input("Enter payment amount: "))

        wallet.make_payment(amount)

    else:
        print("Wallet not found.")


# Check wallet balance
def check_wallet_balance():

    wallet_id = int(input("Enter wallet ID: "))

    wallet = find_wallet(wallet_id)

    if wallet is not None:
        wallet.check_balance()

    else:
        print("Wallet not found.")


# Main program
while True:

    print("\n===== DIGITAL WALLET SYSTEM =====")
    print("1. Create Wallet")
    print("2. View Wallet")
    print("3. Add Money")
    print("4. Make Payment")
    print("5. Check Balance")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_wallet()

    elif choice == 2:
        view_wallet()

    elif choice == 3:
        add_money()

    elif choice == 4:
        make_payment()

    elif choice == 5:
        check_wallet_balance()

    elif choice == 6:
        print("Thank you for using Digital Wallet System!")
        break

    else:
        print("Invalid choice. Please enter 1-6.")



                    


        