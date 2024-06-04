from abc import ABC,abstractmethod
class Bank:
    bankrupt=False
    loanisActive=True
    account=[]
    loan=[]
    

    def __init__(self,name):
        self.name=name
        
class Account:
    

    def __init__(self,name,email,address,acc_type):
        self.name=name
        self.email=email
        self.address=address
        self.acc_type=acc_type
        self.balance=0
        self.acc_num=self.name+self.email
        self.trans_his=[]

        
    
    def show_acc_num(self):
        print(self.acc_num)

    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            self.trans_his.append([f"Deposited amount ${amount}"])
        else:
            print("Invalid amount")
            self.trans_his.append([f"Invalid amount ${amount}"])

    def withdraw(self,amount):
        if Bank.bankrupt==False:
            if amount<=self.balance:
                self.balance-=amount
                self.trans_his.append([f"Withdraw amount ${amount}"])
            else:
                print("Withdrawal amount exceeded")
                self.trans_his.append([f"Withdrawal amount ${amount} exceeded"])
        else:
            print("The bank is bankrupt")

    def transfer_amount(self,amount,another_email):
        val=0
        if Bank.bankrupt==False and amount<=self.balance:
            for i in Bank.account:
                if i.email==another_email:
                    val=1
                    i.balance+=amount
                    self.balance-=amount
                    break
                else:
                    continue
            if val==1:
                print('Tranfered money Successfully')
            else:
                print('Account does not exist')
        else:
            print("The bank is bankrupt")
    
    
    
    def check_trans_his(self):
        for i in self.trans_his:
            print(i)


    @abstractmethod
    def check_balance(self):
        pass

    


class SavingAccount(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address,'savings')
        Bank.account.append(self)
        

        
    def check_balance(self):
        print(f'{self.acc_type} Account Balance is ${self.balance}')



class CurrentAccount(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address,'current')
        Bank.account.append(self)
        self.limit=2

    def check_balance(self):
        print(f'{self.acc_type} Account Balance is ${self.balance}')

    def take_loan(self,amount):
        if self.limit>0 and Bank.bankrupt==False and Bank.loanisActive==True:
            self.balance+=amount
            Bank.loan.append(amount)
            self.limit-=1
            print(f'Congratulations for taking loan')
        elif Bank.bankrupt==True:
            print("The bank is bankrupt")
        elif Bank.loanisActive==False:
            print("Sorry the loan is not available")
        else:
            print("You already taken loan almost 2 times")

class Admin(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address,'Admin')
    
    def create_acc(self):
        Bank.account.append(self)


    def delete_acct(self,another_email):
        for j in Bank.account:
            if j.email==another_email:
                Bank.account.remove(j)
                break
            else:
                print(f'{another_email} does not exist')
                break

    def show_user_list(self):
        for i in Bank.account:
            print(f'{i.name}, {i.email}, {i.address}, {i.acc_type}, {i.acc_num}')

    def check_balance(self):
        total=0
        for i in Bank.account:
            total+=i.balance
        print(total)
    
    def total_loan(self):
        t=0
        for i in Bank.loan:
            t+=i
        print(t)
    
    def bank_rupt(self,cmmnd):
        if cmmnd==True:
            Bank.bankrupt=cmmnd
        else:
            Bank.bankrupt=cmmnd
        
    def loan_feature(self,cmmnd):
        if cmmnd==True:
            Bank.loanisActive=cmmnd
        else:
            Bank.loanisActive=cmmnd


currentuser=None
bank=Bank("MK Bank PLC")
while True:
    print(f'--------------{bank.name}---------------')
    if currentuser==None:
        print('\n No user logged in! \n')
        ch=input('Login or Register? (L\R): ')
        if ch=='R':
            name=input('Name: ')
            email=input('Email: ')
            add=input('Address: ')
            a=input('Savings or Current or Admin? (sv\ cu\ ad): ')
            if a=='sv':
                currentuser=SavingAccount(name,email,add)
            elif a=='cu':
                currentuser=CurrentAccount(name,email,add)
            elif a=='ad':
                currentuser=Admin(name,email,add)
            else:
                print('Invalid choice')
        elif ch=='L':
            ac_email=input('Account Email: ')
            for account in Bank.account:
                if ac_email==account.email:
                    currentuser=account
                    break
    else:
        print(f'Welcome {currentuser.name}')
        if currentuser.acc_type=='savings':
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Available Balance')
            print('4. Check Transcation History')
            print('5. Transfer money')
            print('6. Logout')

            op=int(input("Choose Option: "))
            
            if op==1:
                amount=int(input('Enter the amount: '))
                currentuser.deposit(amount)
            elif op==2:
                amount=int(input('Enter the amount: '))
                currentuser.withdraw(amount)
            elif op==3:
                currentuser.check_balance()
            elif op==4:
                currentuser.check_trans_his()
            elif op==5:
                amount=int(input('Enter the amount: '))
                account_email=input('Enter Account Email: ')
                currentuser.transfer_amount(amount,account_email)
            elif op==6:
                currentuser=None
        elif currentuser.acc_type=='current':
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Available Balance')
            print('4. Check Transcation History')
            print('5. Transfer money')
            print('6. Take loan')
            print('7. Logout')

            op=int(input("Choose Option: "))
            
            if op==1:
                amount=int(input('Enter the amount: '))
                currentuser.deposit(amount)
            elif op==2:
                amount=int(input('Enter the amount: '))
                currentuser.withdraw(amount)
            elif op==3:
                currentuser.check_balance()
            elif op==4:
                currentuser.check_trans_his()
            elif op==5:
                amount=int(input('Enter the amount: '))
                account_email=input('Enter Account Email: ')
                currentuser.transfer_amount(amount,account_email)
            elif op==6:
                amount=int(input('Enter the amount: '))
                currentuser.take_loan(amount)
            elif op==7:
                currentuser=None

        else:
            print('1. Create Account')
            print('2. Delete User Account')
            print('3. Show All Users')
            print('4. Check Available Balance')
            print('5. Check Total loan')
            print('6. (On/Off) loan')
            print('7. (On/Off) Bankrupt')
            print('8. Logout')

            op=int(input("Choose Option: "))
            
            if op==1:
                currentuser.create_acc()
            elif op==2:
                accnt=input("Enter the Account number: ")
                currentuser.delete_acct(accnt)
            elif op==3:
                currentuser.show_user_list()
            elif op==4:
                currentuser.check_balance()
            elif op==5:
                currentuser.total_loan()
            elif op==6:
                cmmnd=input('Press (T/F) :')
                if cmmnd=='T':
                    currentuser.loan_feature(True)
                else:
                    currentuser.loan_feature(False)
            elif op==7:
                cmmnd=input('Press (T/F) :')
                if cmmnd=='T':
                    currentuser.bank_rupt(True)
                else:
                    currentuser.bank_rupt(False)

            elif op==8:
                currentuser=None






    



    

    


    


        
