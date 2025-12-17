class Bank :
    def  __init__(self):
        print("Welcome to the bank" , "taking the customer details as per rules",sep="\n")
        customer_name=input("Enter your name: ")
        customer_id = int(input("enter  customer id: "))
        self.name=customer_name
        self.id=customer_id

    

        
    def create_account(self):
        name=input("Enter your name: ")
        accno=int(input("Enter your account number: "))
        pin=int(input("Set your 4 digit pin: "))
        self.balance = 0
        print("Createing bank Account")
        print(f"Account holder name: {name}")
        print(f"Account number: {accno}")
        print(f"currnent balance: {self.balance}")
        print("Account created successfully")

    def authenticate(self, entered_accno , entered_pin):
        entered_accno=int(input("Enter your account number: "))
        entered_pin=int(input("Enter your 4 digit pin: "))
        if entered_accno == self.accno and entered_pin == self.pin:
            return True
        else:
            print("Invalid PIN")
            return False

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Please collect your cash")
        elif amount>self.balance:
            print("insiffecient amount in you bank balance")
        else:
            print("insiffecient balance")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("amount is deposited seccessfully")
        else:
            print("invalid amount")

    def checkbalance(self):
        print(f"you balance is: {self.balance}")

        
one = Bank()



while True:
    print("----bank SYSTEM----")
    print("Welcome to the bank System" , "what services do you want",sep="\n")
    print("1.create account","2.Withdraw", "3.Deposit", "4.Check Balance", "5. exit", sep="\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        one.create_account()
    elif choice==2:
        amount=int(input("Enter amount to withdraw: "))
        one.withdraw(amount)
    elif choice==3:
        amount=int(input("enter the amount for deposit: "))
        one.deposit(amount)
    elif choice==4:
        one.checkbalance()
    elif choice==5:
        print("thank you for visiting the bank")
        print("exiting......")
        break
    else:
        print("invalid choice")