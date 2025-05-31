
class Account:
    def __init__(self, account: str, balance: int) -> None:
        self.account = account
        self.__balance = balance
        
    def get_balance(self) -> int:
        return self.__balance
        
    def deposit(self, amount) -> None:
        self.__balance += amount
        print(f"\n{amount} deposited successfully.\n")
        
    def withdraw(self, amount) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"\n{amount} withdraw successfully.\n")
        else:
            print("Insufficient balance!")
            
class InterestAccount(Account):
    def __init__(self, account: str, balance: int, interest_rate: float) -> None:
        Account.__init__(self, account, balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self) -> float:
        return self.get_balance() * self.interest_rate


class Transacions:
    def __init__(self) -> None:
        self.transactions: list = []
        
    def add_transaction(self, transaction: str) -> None:
        self.transactions.append(transaction)
        
    def history(self) -> None:
        for index, transaction in enumerate(self.transactions):
            print(f"#{index+1}. {transaction}")
   
   
class SavingAccount(InterestAccount, Transacions):
    def __init__(self, account: str, balance: int, interest_rate: float) -> None:
        InterestAccount.__init__(self, account, balance, interest_rate)     
        Transacions.__init__(self)     
   
        
savings: SavingAccount = SavingAccount("A02", 100000, 1.2)


savings.deposit(40000)

print(f"Balance: {savings.get_balance()}")
savings.withdraw(80000)
interest = savings.calculate_interest()
savings.add_transaction("Deposit: 40000")
savings.add_transaction("Withdraw: 80000")


print(f"Balance: {savings.get_balance()}")
savings.history()