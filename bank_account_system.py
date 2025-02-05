# ### **Bank Account System**

# - **Concepts:** Object-Oriented Programming (OOP).
# - **Key Features:** Deposit, withdrawal, transaction history.
# - **What You’ll Learn:**
#     - Classes and objects (`class BankAccount`)
#     - Encapsulation (private attributes)
#     - File handling for transaction history


class BankAccount: 
    def __init__(self, accountNumber, accountType, amount, transaction):
        self.__accountNumber = accountNumber
        self.__accountType = accountNumber
        self.__amount = amount
        self.__transaction = transaction


    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def getAccountNumber(self):
        return self.__accountNumber

    def setAccountType(self,accountType):
        self.__accountType = accountType

    def getAccountType(self):
        return self.__accountType

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setTransactions(self,transaction):
        self.__transaction = transaction

    def getTransaction(self):
        return self.__transaction

    def display(self):
        print("********Account Information********")
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Type: {self.__accountType}")
        print(f"Amount: {self.__amount}")
        print(f"Transactions: {self.__transaction}")






