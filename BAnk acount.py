class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self._balance = balance
    def bygetter(self):
        return self._balance
    def bysetter(self,amount):
        if amount>=0:
            self._balance = amount
        else:
            print("invalid amount")
obj = BankAccount("vikram",6644)
print(obj.bygetter())
obj.bysetter(500000)
print(obj.bygetter())
