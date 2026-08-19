class Bank:
    def __init__(self):
        self.accounts={}  #created dictionary to store as key
        self.next_acc_no=1001

    def register(self, name, age, location):
        acc_no=self.next_acc_no
        self.next_acc_no=self.next_acc_no+1
        
        new_acc=Account(acc_no, name, age, location)
        self.accounts[acc_no]=new_acc
        print(f"Account created successfully. Your Account Number is: {acc_no}")
        return acc_no

    def login(self, acc_no):
        try:
            account=self.accounts[acc_no]
            print("Login Success")
            return account
        except KeyError:
            print("Invalid Account Number")

class Account:
    def __init__(self, acc_no, name, age, location):
        self.acc_no=acc_no
        self.name=name
        self.age=age
        self.location=location
        self.balance=0
    def deposit(self, amount):
        self.balance=self.balance + amount
        print("Amount deposited")
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance=self.balance - amount
            print("Amount Withdrawn")
        else:
            print("Insufficient balance")
    def total_balance(self):
        print(str(self.balance))

    def payment(self, receiver_acc, amount, bank):
        try:
            if amount>self.balance:
                print("Insufficient balance")
                
            receiver=bank.accounts[receiver_acc]

            self.balance=self.balance - amount
            receiver.balance=receiver.balance + amount
            print(f"Transferred Rs. {amount} to Account No. {receiver_acc}. Your balance is {self.balance}")
        except KeyError:
            print("No receiver")

b=Bank()

while True:
    req=int(input("1. Register || 2. Login || 0. Exit"))

    if req==0:
        print("Thank you")
        break

    elif req==1:
        name=input("Enter your name: ")
        age=input("Enter your age: ")
        location=input("Enter your location: ")
        b.register(name, age, location)

    elif req==2:
        acc_no=int(input("Enter your account no: "))
        account=b.login(acc_no) 
        if account:
            while True:
                choice=int(input("1. Deposit, 2. Withdraw, 3. Balance, 4. Payment, 0.Exit: "))
                if choice==0:
                    print("Thank you")
                    break
                elif choice==1:
                    depo=float(input("Enter the deposit amount: "))
                    account.deposit(depo)
                elif choice==2:
                    withd=float(input("Enter the amount to withdraw: "))
                    account.withdraw(withd)
                elif choice==3:
                    print(f"Your Balance: {account.balance}")
                elif choice==4:
                    receiver= int(input("Enter the receiver account number: "))
                    amount=float(input("Enter the amount to transfer: "))
                    account.payment(receiver, amount, b)
