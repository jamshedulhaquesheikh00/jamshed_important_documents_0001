
class Bank:
    bank_name = "Default Bank"  # Class variable

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_info(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

# Create two customers
cust1 = Bank("Jamshed")
cust2 = Bank("Bob")

# Show initial bank name
cust1.show_info()
cust2.show_info()

# Change bank name using class method
Bank.change_bank_name("Muslim Bank")

# Show updated bank name for both instances
cust1.show_info()
cust2.show_info()
