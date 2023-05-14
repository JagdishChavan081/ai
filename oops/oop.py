class ATM:
    # constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
        Hi How can i help You?
         1. press 1 to create pin
         2. press 2 to change pin
         3. press 3 to check balance
         4. press 4 to withdraw
         5. Anything Else to exit
         """
        )

        if user_input == "1":
            # create pin
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()

        elif user_input == "4":
            #
            self.withdraw()
        else:
            exit()

    # write a function to create pin
    def create_pin(self):
        user_pin = input("enter your pin")
        self.pin = user_pin

        user_balance = int(input("enter balance"))
        self.balance = user_balance

        print("pin created sucessfully")
        self.menu()

    # write a function to change pin
    def change_pin(self):
        old_pin = input("enter old pin")

        if old_pin == self.pin:
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("print change successfull")
            self.menu()
        else:
            print("Wrong Input")
            self.menu()

    # check balance
    def check_balance(self):
        user_pin = input("enter your pin")
        if user_pin == self.pin:
            print("Your balance is:", self.balance)
            self.menu()
        else:
            print("Enter correct pin")
            self.menu()

    # withdrawal
    def withdraw(self):
        user_pin = input("enter your pin")
        if user_pin == self.pin:
            amount = int(input("Ente the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("withdrawal successful, \n current balance:", self.balance)
            else:
                print("insufficient funds")
        else:
            print("Enter correct pin")
        self.menu()


# create an object

obj = ATM()
