class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen, battery):
        super().__init__(name, price, stock, warranty)
        self.screen = screen
        self.battery = battery

    def __str__(self):
        return f"Smartphone: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months, Screen: {self.screen} inches, Battery: {self.battery} hours"
        