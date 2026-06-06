#new atm pro.

# main ATM MASCHIN
class password:  
    Account_numbar = " "
    while True:
        print(int(input("enter account_number : ")))
        if "account_number" == 'account_number':
            break
        else:
            print("plesas enter coreact number")
    
class Account:

    holder_name = "dipesh verma"

    def __init__(self,account_number,pin,balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def pin(self) :
     pin = "1234 "
    while True:
            if "pin" == 'pin':
               break
            else:
                print("plesas enter coreact pin ")

    def debit(self,amount):
        amount -= self.balance
        print("debit", "rs = ", amount)

    def credit(self,amount):
        amount += self.balance
        print("credit", "rs = ", amount)


    def check_balance(self):
        print(self.balance)
        return self.balance
    

s2 = password()

print(Account.holder_name)
s1 = Account( 9669563475 , 1234, 100000)
print(Account.pin(int(input("enter your pin :"))))

print(s1.account_number)
print(s1.pin)

s1.debit(int(input("enter your debit amount :")))
s1.credit(int(input("enter your credit amount :")))
s1.check_balance()