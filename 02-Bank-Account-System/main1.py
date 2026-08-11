class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print("successfully deposit")

        else:
            print("invalid")

        
    def withdraw(self,amount):
        if amount<=0:
            print("invalid")
        elif amount> self.balance:
            print("insufficent balance")  
        else:

            self.balance -= amount
            print("successfully withdarwn")
          
    def check_balance(self):
        print(self.balance)
    def display(self):
        print(self.name)
        print(self.account_number)
        print(self.balance)  


accounts = []
def create_account():
    name = input("Enter name:")
    account_number = int(input("Enter account number:"))
    balance = float(input("Enter starting balance:"))
    account = BankAccount(name, account_number, balance)
    accounts.append(account)

    print("Account created successfully!")
def find_account(account_number):
    for account in accounts:   
        if(account.account_number == account_number):
            return account
    return None
def deposit_money():
    account_number = int(input("Enter account number: "))

    account = find_account(account_number)

    if account is not None:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    else:
        print("invalid")
def withdraw_money():
    account_number = int(input("Enter account number: "))

    account = find_account(account_number)

    if account is not None:
        amount = float(input("Enter  withdraw amount: "))
        account.withdraw(amount)
    else:
        print("invalid") 
def check1_balance():
    account_number = int(input("Enter account number: "))

    account = find_account(account_number)

    if account is not None:
        amount = float(input("Enter  check balance: "))
        account.check_balance()
    else:
        print("invalid") 
def display1():
    account_number = int(input("Enter account number: "))

    account = find_account(account_number)

    if account is not None:
        
        account.display()
    else:
        print("invalid")                




while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        deposit_money()

    elif choice == 3:
        withdraw_money()

    elif choice == 4:
        check1_balance()

    elif choice == 5:
        display1()

    elif choice == 6:
        print("Thank you for using Bank Account System!")
        break

    else:
        print("Invalid choice")