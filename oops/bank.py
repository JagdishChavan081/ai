# Bank Class
# Create a Python class called BankAccount which represents a bank account, having as attributes:
# accountNumber (numeric type), name (name of the account owner as string type), balance.
class BankAccount:
    # Create a constructor with parameters: accountNumber, name, balance.
    def __init__(self):
        self.accountNumber = ""
        self.name = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
        Hi How can i help you?
        1. press 1 to create account
        2. press 2 to make deposit
        3. press 3 to withdraw amount
        4. press 4 to display details
        """
        )

        if user_input == "1":
            # create account
            self.CreateAccount()
        elif user_input == "2":
            # makedeposit
            self.MakeDeposit()
        elif user_input == "3":
            # withdraw amount
            self.Withdrawal()
        elif user_input == "4":
            # diaplay details
            self.DisplayDetails()
            pass
        else:
            exit()

    # write a function to create account
    def CreateAccount(self):
        self.accountNumber = input("write account number you like to have")
        self.name = input("Enter your name")
        self.balance = int(input("Enter your initial balance"))

        print(
            "\nAccount Number:",
            self.accountNumber,
            "\nName:",
            self.name,
            "\nBalance:",
            self.balance,
        )
        self.menu()

    # Create a Deposit() method which manages the deposit actions.
    def MakeDeposit(self):
        account_number = input("enter your accont number")

        if account_number == self.accountNumber:
            amount = int(input("Enter Deposit amount"))
            if amount > 0:
                self.balance = self.balance + amount
                print("Your Deposit amount is: ", amount)
                print("Your current balance is", self.balance)
            else:
                print("Enter amount greater than 0")
        else:
            print("please Enter valid account Number")
        self.menu()

    # Create a Withdrawal() method which manages withdrawals actions.
    def Withdrawal(self):
        account_number = input("Enter your Account Number")

        if account_number == self.accountNumber:
            withdraw = int(input("Enter amount you want to withdraw: "))
            if withdraw > 0 and withdraw <= self.balance:
                self.balance = self.balance - withdraw
                print("Your Withdra amount is: ", withdraw)
                print("Your current balance is: ", self.balance)
            elif withdraw > self.balance:
                print("Insufficient Funds")
            else:
                print("Enter valid amount")
        else:
            print("please enter valid account number")
        self.menu()

    # Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
    def bankFees(self):
        fees = self.balance * 0.05
        print("Your anual bank account maintenance fees will be:", fees)
        self.menu()


# Create a display() method to display account details. Give the complete code for the BankAccount class.
def DisplayDetails(self):
    print("Your account details are as follow:")
    print("Your Account Number:", self.accountNumber)
    print("Your Name:", self.name)
    print("Your current balance:", self.balance)


# object
acc1 = BankAccount()
