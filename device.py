class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months")

    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months"

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            print(f"Stock reduced by {amount}. Remaining stock: {self.stock}")
        else:
            print("Not enough devices.")