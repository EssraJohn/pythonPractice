class Account:

    def __init__(self, cust_id, name, initial_bal=0):
        self.id = cust_id
        self.name = name
        self.balance = initial_bal

    def get_balance(self):
        return self.balance

    def credit_balance(self, amount):
        amount = self.balance + amount
        return amount


customer1 = Account("191", "Essra")
print(customer1.id, customer1.name, customer1.balance)
print(customer1.get_balance())
print(customer1.credit_balance(3999))
