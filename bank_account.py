import datetime
class BankAccount:
    def __init__(self, account_holder, balance, overdraft_limit=-500):
        self.__account_holder = account_holder
        self.__balance = balance
        self.__overdraft_limit = overdraft_limit
        self.__transaction_history = []

    def deposit(self, amount):
        if amount < 0:
            print('Amount should be positive.')
            return
        self.__balance += amount
        self.__transaction_history.append(f"Deposited: {amount}, Date: {datetime.datetime.now()}")
        print(f"Successfully Deposited: {amount}, Current Balance is ${self.__balance}")

    def withdraw(self, amount):
        if amount < 0:
            print('Amount should be positive.')
            return
        elif self.__balance - amount < self.__overdraft_limit:
            print(f'Insufficient funds. You can withdraw up to {self.__balance - self.__overdraft_limit}.')
            return
        self.__balance -= amount
        self.__transaction_history.append(f"Withdrew: {amount}, Date:  {datetime.datetime.now()}")
        print(f"Successfully Withdrew: {amount}, Current Balance is ${self.__balance}")

    def apply_interest(self, rate):
        if rate < 1:
            print('Interest should be greater than 0.')
            return
        interest = self.__balance * (rate / 100)
        self.__balance += interest
        self.__transaction_history.append(f'Interest applied: {interest}, Date:  {datetime.datetime.now()}')
        print(f'{interest} Interest applied successfully, current balance is {self.__balance}')

    # Method to display the transaction history with numbers
    def get_transaction(self):
        if not self.__transaction_history:
            print("No transactions available.")
        else:
            for idx, transaction in enumerate(self.__transaction_history, 1):
                print(f"{idx}. {transaction}")

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder


# Creating a BankAccount object
account = BankAccount("Alice", 1000)

# Perform some transactions
account.deposit(500)
account.withdraw(200)
account.apply_interest(5)

# Display transaction history
account.get_transaction()
