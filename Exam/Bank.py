
class User():

    def __init__(self, name, email, password, initial_balance=0):
        self.name = name
        self.email = email
        self.__password = password
        self.user_balance = initial_balance
        self.all_transaction = []

    def deposite(self, amount):
        if amount > 0:
            self.user_balance += amount
            self.all_transaction.append(f'Successflly Desposite {amount} taka')
            bank.bank_balance += amount
            print(f'{self.name} deposite {amount} taka Successfully!')
        else:
            print('You Entired invalid amount.Please Try Again')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.user_balance:
            self.user_balance -= amount
            self.all_transaction.append(f'Successflly Withdraw {amount} taka')
            bank.bank_balance -= amount
            print(f'{self.name} withdraw {amount} taka Successfully!')
        else:
            print('Insufficient balance')

    def transfer_taka(self, sender, receiver, amount):
        if amount < sender.user_balance:
            sender.user_balance -= amount
            receiver.user_balance += amount
            self.all_transaction.append(f'Successflly Send {amount} taka to {receiver.name} Account')
            receiver.all_transaction.append(f'Successflly Receive {amount} taka from {self.name} Account')
            print(
                f'{sender.name} Successfully send {amount} taka to {receiver.name} account')
            print(
                f'{receiver.name} Successfully receive {amount} taka from {sender.name} account')

        else:
            print('Insufficient balance for transfer taka')

    def check_balance(self):
        print(f'{self.name} Current balance is: {self.user_balance}')

    def transaction_history(self):
        print(f'<----------Transaction History of {self.name} is:----------->')
        print(f'Initial deposite:{bank.initial_deposit}')
        for transaction in self.all_transaction:
            print(transaction)

    def take_loan(self, amount):
        if bank.loan_feature == False:
            print('Sorry!!The bank loan feature has been Off')
        else:
            if amount > self.user_balance*2 or amount < 0:
                print('Something is wrong.Please try again!!')
            else:
                self.user_balance += amount
                self.all_transaction.append(f'Take loan {amount} taka')
                bank.bank_balance -= amount
                bank.total_loan += amount
                print(f'{self.name} {amount} taka take loan ')


class Admin():
    all_users = []
    bank_balance = 0
    total_loan = 0
    loan_feature = True

    def __init__(self, name):
        self.name = name

    def create_new_account(self, name, email, password, initial_deposit=0):
        user = User(name, email, password, initial_deposit)
        self.all_users.append(user)
        self.initial_deposit = initial_deposit
        self.bank_balance += initial_deposit
        return user

    def total_bank_balance(self):
        print(f'Total Bank Balance is:{self.bank_balance}')

    def total_loan_amount(self):
        print(f'Total Loan Amount is:{self.total_loan}')
    
    def control_loan_feature(self,status):
        if(status == False):
            self.loan_feature = False
        else:
            self.loan_feature = True
            






bank = Admin('Islami Bank')
Shaon = bank.create_new_account('Shaon', 'abc@gmail.com', 121, 1000)
Roni = bank.create_new_account('Roni', 'roni@gmail.com', 211, 1000)

#User Part
# --------Check deposite,Withdraw ,Transfer,transaction History,check balance and take loan------------
Shaon.deposite(2000)
Roni.deposite(2000)
Shaon.withdraw(300)
Roni.withdraw(200)
Shaon.transfer_taka(Shaon, Roni, 500)
Roni.transfer_taka(Roni,Shaon,300)

Shaon.transaction_history()
Shaon.check_balance()

Roni.transaction_history()
Roni.check_balance()

Shaon.take_loan(200)
Roni.take_loan(300)
Shaon.transaction_history()
Shaon.check_balance()


#Admin part
# Check total bank balance,Total Loan amount,On_Off Loan feature
bank.total_bank_balance()
bank.total_loan_amount()

bank.control_loan_feature(False)
Shaon.take_loan(100)

