from abc import ABC, abstractmethod
class BankAccount(ABC):
    # abstract method
    def transcation(self):
        pass
class Account(BankAccount):
    def __init__(self, account_holder,account_number,balance=0.0):
        self.account_holder = account_holder
        self._account_number = account_number
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >=0:
            self.__balance = amount
        else:
            print("balance cannot be negative")
    
    def sef_info(self):
        print(f"account holder name : {self.account_holder}")
        print(f"account number : {self._account_number}")
        print(f"acount blance : {self.__balance}")

    # Override parent method
    def transaction(self):
        print("Transaction method in ATM class is handling the flow.")

class ATM(Account):
    bank_name = "ABC Bank"
    def __init__(self, account_holder, account_number, balance=0.0,pin = "1234"):  #cunstructor of ATM class
        #calling parent class constructor
        super().__init__(account_holder, account_number, balance)
        self.__pin = pin # pin should be private

    # class method
    def bank_name_info(cls):
        print(f"welcome to the {cls.bank_name}")
    
    #static method
    def validate_amount(self,amount):
        if amount > 0:
            return True
        else:
            print("no amount in your account pleae deposit first")
            return False
        
    #instance method
    def check_balance(self):
        print(f"your current balance is : {self.get_balance()}")
    
    #doposit method for depositing the amount in the account
    def deposit(self, amount):
        if self.validate_amount(amount):
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print(f"deposit successful! new balance is : {self.get_balance()}")
        else:
            print("deposit faild !, please enter valid amount next time!")

    # withdraw method for withdraw the amount from the account
    def withdraw(self, amount,pin):
        if pin == self.__pin:
            if self.validate_amount(amount):
                if amount <= self.get_balance():
                    new_balance = self.get_balance() - amount
                    self.set_balance(new_balance)
                    print(f"withdraw is succesfully completes!")
                    print(f" new balance is : {new_balance}")
                else:
                    print("insufficient balance! in your acount do diposit first")
            else:
                print("withdraw is failde please ener a valid amount next time for widthdraw")
        else:
            print("pin is incorrect please check once again before entering the pin")
    
    # account details
    def account_details_info(self):
        print(f"bank name : {self.bank_name}")
        print(f"account holder name : {self.account_holder}")
        print(f"account number : {self._account_number}")
        print(f"account balance : {self.get_balance()}")

    def verify_pin(atm_obj):
        for i in range(3):
            pin = input("enter your pin : ")
            if pin == atm_obj.__pin:
                print("pin verified successfully!")
                return True
            else:
                print("incorrect pin please try again")
                return False
    
    def atm_menu(self):
        print("--------WELCOME TO ATM SYSTEM--------")
        atm_obj.bank_name_info()
        print("--------------------------------")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self._account_number}")
        print("--------------------------------")

atm_obj = ATM("John Doe", "1234567890", 1000.0, "1234")
atm_obj.transaction()
atm_obj.atm_menu()

while True:
    print("\n-----------------------------")
    print("ATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")
    print("-----------------------------")

    choice = input("Enter your choice: ")
    if choice == '1':
        print("-----------------------------")
        print("Balance Money")
        print("-----------------------------")
        atm_obj.check_balance()
    elif choice == '2':
        print("-----------------------------")
        print("DEPOSIT MONEY")
        print("-----------------------------")
        amount = float(input("Enter amount to deposit: "))
        atm_obj.deposit(amount)
    elif choice == '3':
        print("-----------------------------")
        print("WITHDRAW MONEY")
        print("-----------------------------")
        amount = float(input("Enter amount to withdraw: "))
        pin = input("Enter your PIN: ")
        atm_obj.withdraw(amount, pin)
    elif choice == '4':
        print("-----------------------------")
        print("Account Details")
        print("-----------------------------")
        atm_obj.account_details_info()
    elif choice == '5':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")