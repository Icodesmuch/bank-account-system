# ### **Bank Account System**

# - **Concepts:** Object-Oriented Programming (OOP).
# - **Key Features:** Deposit, withdrawal, transaction history.
# - **What You’ll Learn:**
#     - Classes and objects (`class BankAccount`)
#     - Encapsulation (private attributes)
#     - File handling for transaction history
import random

class BankAccount: 
    def __init__(self, accountType, amount):
        self.__accountNumber = BankAccount.generateAccountNumber()
        self.__accountType = accountType
        self.__amount = amount
        self.__transactions = []


    @property    
    def acccountNumber(self):
        return self.__accountNumber

    def generateAccountNumber():
        # Implementation for generating account number
        return random.randint(1000000000, 9999999999)
    
    @property
    def getAccountType(self):
        return self.__accountType

    def setAmount(self, amount):
        self.__amount = amount

    @property
    def getAmount(self):
        return self.__amount

    # def setTransactions(self,transaction):
    #     self.__transaction = transaction

    @property
    def getTransaction(self):
        return self.__transaction

    def bankMenu(self):
        print("Welcome to our Banking System")
        print('Choose an option below')
        print('1. Login')
        print('2. Create Account')
        option = str(input('-> '))

        if option == '1':

            print('\n*******Login*******')
            print('Enter Account number: ')
            accountnumber = input('-> ')


    
    def atmMenu():

        while True:
            print('ATM Menu')
            num = int(input('Enter your account number: '))

            #check if num is present in database


    def displayAccountInfo(self):
        print("\n********Account Information********")
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Type: {self.__accountType}")
        print(f"Amount: ${self.__amount}")
        print(f"Transactions: {self.__transaction}")






if __name__ == '__main__':
    ncb = BankAccount('Savings', 23675439)
    ncb.bankMenu()

