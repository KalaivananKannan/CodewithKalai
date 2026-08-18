print("***Welcome to BOB Banking***")
class Bank:
	balance=0 # feature
	
	def deposit(self, amount):   # attribute
		self.balance=self.balance+amount

	def withdraw(self, amount):  # attribute
		self.balance=self.balance-amount

	def display_balance(self):  # attribute
		print(str(self.balance))

s=Bank()

while True:
	type=int(input("press 1-Deposit, 2-Balance, 3-Withdraw, 0-exit: "))

	if type==0:
		print("Thank you")
		break
	if type==1:
		depo=float(input("Enter the deposit amount: "))
		s.deposit(depo)
		print("Amount deposited. Thank you!")
	if type==2:
		s.display_balance()
	if type==3:
		amount=float(input("Enter the amount to withdraw: "))
		if amount > s.balance:
			print("Insufficient balance")
		else:
			s.withdraw(amount)
			print("Amount withdrawn. Thank you for choosing BOB Banking.")
	if type>3:
		print("Invalid option!!. Please choose correct option")
