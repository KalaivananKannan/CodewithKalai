import mysql.connector
import re, threading, time
from datetime import datetime

print("  *** Welcome to IDBI banking !!!   ")
def val_name(name):
    if re.search("^[A-Za-z ]+$", name):
        return True
    else:
        print("Name should be only in alphabets")
        return False

def val_age(age):
    if re.search("^[0-9]{1,3}$", age):
        return True
    else:
        print("Age should be only in numbers")
        return False

class Transaction:
    def __init__(self, amount, acc_no):
        self.amount=amount
        self.acc_no=acc_no
        self.timestamp=datetime.now().strftime('%A, %d %B %Y %H:%M:%S')
    def details(self):
        return f"Transaction of {self.amount} at {self.timestamp}"

class Deposit(Transaction):
    def details(self):
        return f"Deposited {self.amount} at {self.timestamp}"

class Withdraw(Transaction):
    def details(self):
        return f"Withdrew {self.amount} at {self.timestamp}"

class Payment(Transaction):
    def __init__(self, amount, sender_acc, receiver_acc):
        super().__init__(amount, sender_acc)
        self.receiver_acc=receiver_acc
    def details(self):
        return f"Transferred {self.amount} to {self.receiver_acc} at {self.timestamp}"

class Receive(Transaction):
    def __init__(self, amount, sender_acc, receiver_acc):
        super().__init__(amount, receiver_acc)
        self.sender_acc=sender_acc
    def details(self):
        return f"Received {self.amount} from {self.sender_acc} at {self.timestamp}"

class Bank:
    def __init__(self):
        self.accounts=[]
        self.next_accno=3810000100
        self.filename="bankacc.txt"
        self.logged_in_accounts=set()
        self.conn=mysql.connector.connect(
            host="localhost", user="root", password="KalaiSql123#", database="Banking"
        )
        self.cursor=self.conn.cursor()
        self.load_accounts()
      

    def save_accounts(self):
        with open(self.filename, "w") as f:
            for acc in self.accounts:
                line=f"{acc['acc_no']}|{acc['username']}|{acc['password']}|{acc['name']}|{acc['age']}|{acc['location']}|{acc['balance']}\n"
                f.write(line)

            for acc in self.accounts:
                sql=""" REPLACE INTO Accounts(acc_no, username, password, name, age, location, balance)
                    values(%s,%s,%s,%s,%s,%s,%s)"""
                values=(acc["acc_no"], acc["username"], acc["password"], acc["name"], acc["age"], acc["location"], acc["balance"])
                self.cursor.execute(sql, values)
            self.conn.commit()

    def load_accounts(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    acc_no, username, password, name, age, location, balance=line.strip().split("|")
                    acc={
                        "acc_no":int(acc_no), "username":username,
                        "password":password, "name":name, "age":int(age),
                        "location":location, "balance":float(balance),
                        "transactions":[]
                    }
                    self.accounts.append(acc)
                if self.accounts:
                    self.next_accno=self.accounts[-1]["acc_no"]+1
        except FileNotFoundError:
            pass

    def register(self, username, password, name, age, location):
        acc={
            "acc_no":self.next_accno,
            "username": username, "password": password,
            "name":name, "age": age, "location": location,
            "balance":0,
            "transactions":[]
        }
        self.accounts.append(acc)        
        print(f"\nAccount created successfully.\nYour Account Number is: {self.next_accno}\n")
        self.next_accno=self.next_accno+1
        self.save_accounts()

    def login(self, username, password):
        for i in self.accounts:
            if i["username"]==username and i["password"]==password:
                print("Login success\n")
                self.logged_in_accounts.add(i["acc_no"])
                return i
        print("Login failed")
        return None

    def find_account(self, acc_no):
        for a in self.accounts:
            if a["acc_no"]==acc_no:
                return a
        return None

    def log_transaction(self, acc_no, transaction):
        filename=f"transactions_{acc_no}.txt"
        with open(filename, "a") as f:
            f.write(transaction + "\n")

    def update_balance(self, acc_no, balance):
        sql="Update Accounts set balance=%s where acc_no=%s"
        self.cursor.execute(sql, (balance, acc_no))
        self.conn.commit()

    def load_transactions(self, acc_no):
        filename=f"transactions_{acc_no}.txt"
        try:    
            with open(filename, "r") as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            return []

    def login_required(target):
        def check_login(self, acc_no, *args, **kwargs):            
            if acc_no in self.logged_in_accounts:
                return target(self, acc_no, *args, **kwargs)
            else:
                print("Invalid account. Please login first.")
                return None
        return check_login

    @login_required
    def deposit(self, acc_no, amount):
        try:
            acc=self.find_account(acc_no)
            acc["balance"]=acc["balance"] + amount            
            transaction=Deposit(amount, acc_no).details()
            acc["transactions"].append(transaction)
            self.save_accounts()
            self.update_balance(acc_no, acc["balance"])
            self.log_transaction(acc_no, transaction)
            print("Amount deposited successfully")
        except Exception as e:
            print("Error:", e)

    @login_required
    def withdraw(self, acc_no, amount):
        try:
            acc=self.find_account(acc_no)
            if amount<=acc["balance"]:
                acc["balance"]=acc["balance"] - amount
                self.update_balance(acc_no, acc["balance"])
                transaction=Withdraw(amount, acc_no).details()
                acc["transactions"].append(transaction)
                self.save_accounts()
                self.log_transaction(acc_no, transaction)
                print("Amount Withdrawn successfully\n")
            else:
                print("Insufficient balance\n")
        except Exception as e:
            print("Error: ", e)

    @login_required
    def payment(self, sender_acc, receiver_acc, amount):
        try:
            sender=self.find_account(sender_acc)    
            receiver=self.find_account(receiver_acc)
            if amount<=sender["balance"]:
                sender["balance"]=sender["balance"] - amount
                receiver["balance"]=receiver["balance"] + amount
                self.update_balance(sender_acc, sender["balance"])
                self.update_balance(receiver_acc, receiver["balance"])
                k1=Payment(amount, sender_acc, receiver_acc).details()
                k2=Receive(amount, sender_acc, receiver_acc).details()
                sender["transactions"].append(k1)
                receiver["transactions"].append(k2)
                self.save_accounts()
                self.log_transaction(sender_acc, k1)
                self.log_transaction(receiver_acc, k2)
                print("Payment success")
            else:
                print("Insufficient Balance")
        except Exception as e:
            print("Error", e)

    def total_balance(self, acc_no):
        acc=self.find_account(acc_no)
        print(f"Total Balance is: {acc['balance']}")
        
    def history(self, acc_no):
        print("\nTransaction History")
        transactions=self.load_transactions(acc_no)
        for t in transactions:
            print(t)
    
    def show_lastfive_transactions(self, acc_no, n=5):
        transactions=self.load_transactions(acc_no)
        print("Last five transactions: ", transactions[-n:])

b=Bank()

def simulate_deposit(bank, acc_no, amount, delay):
    print(f"Preparing to deposit {amount}...")
    time.sleep(delay)
    print(f"Depositing {amount} now... ")
    bank.deposit(acc_no, amount)
    print(f"Deposit Completed!")
def simulate_withdraw(bank, acc_no, amount, delay):
    print(f"Preparing to withdraw {amount}...")
    time.sleep(delay)
    print(f"Withdrawing {amount} now...")
    bank.withdraw(acc_no, amount)
    print(f"Withdrawal Completed!")

while True:
    req=int(input("1. Register || 2. Login || 0. Exit"))

    if req==0:
        print("Thank you")
        break

    elif req==1:
        username=input("Enter the username: ")
        password=input("Enter the password: ")
        try:
            if re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]).{8,15}$', password):
                print("Password registered\nPlease enter the personal details\n")
                name=input("Enter your name: ")
                age=input("Enter your age: ")
                location=input("Enter your location: ")
                if val_name(name) and val_age(age):
                    b.register(username, password, name, int(age), location)         
                else:
                    print("Registration failed\n")
            else:
                print("\nInvalid!! Password length must be 8-15 characters.\nMust include A-Z, a-z, 0-9, and a special character.\nEx: Abc@1234\n")
        except:
            print("Error. Not able to validate\n")
        
    elif req==2:
        username=input("Enter the username: ")
        password=input("Enter the password: ")
        account=b.login(username, password) 
        if account:
            acc_no=account["acc_no"]
            while True:
                try:
                    choice=int(input(
                        "1. Deposit\t\t"
                        "2. Withdraw\t\t"
                        "3. Balance  \t\t"
                        "4. Payment\n" 
                        "5. All Transactions\t"
                        "6. Mini statement\t"
                        "7. Transaction Demo\t"
                        "0. Exit\n"
                        "Enter your choice: "
                        ))
                except:
                    print("Invalid input. Please enter a number\n")
                    continue

                if choice==0:
                    print("Thank you")
                    break
                elif choice==1:
                    depo=float(input("Enter the deposit amount: "))
                    b.deposit(acc_no, depo)
                elif choice==2:
                    withd=float(input("Enter the amount to withdraw: "))
                    b.withdraw(acc_no, withd)
                elif choice==3:
                    b.total_balance(acc_no)
                elif choice==4:
                    try:
                        receiver= int(input("Enter the receiver account number: "))
                        amount=float(input("Enter the amount to transfer: "))
                        b.payment(acc_no, receiver, amount)
                    except ValueError:
                        print("Enter valid account number")
                elif choice==5:
                    b.history(acc_no)
                elif choice==6:
                    b.show_lastfive_transactions(acc_no)
                elif choice==7:
                    t1=threading.Thread(target=simulate_deposit, args=(b, acc_no, 500, 5))
                    t2=threading.Thread(target=simulate_withdraw, args=(b, acc_no, 100, 3))
                    t1.start()
                    t2.start()
                    t1.join()
                    t2.join()
                else:
                    print("Invalid Choice.")