class Customer:
    def __init__(self, customer_id: int, customer_name: str) -> None:
        self.id = customer_id
        self.name = customer_name
        

class LoyaltyPoints:
    def __init__(self) -> None:
        self.points = 0
        
    def earn_points(self, amount: int) -> None:
        self.points += amount
        
    def redeem_points(self, amount: int) -> None:
        if self.points >= amount:
            self.points -= amount
            
        else:
            print("Insufficient points!")
            
    def show_points(self) -> int:
        return self.points
        
        
class VIPCustomer(Customer, LoyaltyPoints):
    def __init__(self, customer_id: int, customer_name: str) -> None:
        Customer.__init__(self, customer_id, customer_name)
        LoyaltyPoints.__init__(self)
        
class Transaction:
    def __init__(self, transaction_id: int, customer: Customer, amount: str) -> None:
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount
        

class TransactionHistory:
    def __init__(self) -> None:
        self.transactions: list = []
        
    def add_transaction(self, transaction) -> None:
        self.transactions.append(transaction)
        
    def show_transactions(self) -> None:
        for transaction in self.transactions:
            print(transaction.transaction_id, transaction.customer.name, transaction.amount)
            
vip: VIPCustomer = VIPCustomer(1, "Abdullah")
vip.earn_points(20000)
vip.redeem_points(10000)

transaction1: Transaction = Transaction(1, vip, "+40000")
transaction2: Transaction = Transaction(2, vip, "-20000")

transaction_history: TransactionHistory = TransactionHistory()
transaction_history.add_transaction(transaction1)
transaction_history.add_transaction(transaction2)

transaction_history.show_transactions()