class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0  # To track the value of the last transaction

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items += [title] * quantity  # Adds the item based on quantity
        self.last_transaction = price * quantity  # Store last transaction value

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total = self.total - discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0  # Reset last transaction after voiding
        if self.total < 0:
            self.total = 0.0  # Make sure the total doesn't go below 0

