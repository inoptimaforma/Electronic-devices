class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"Tablet: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months, Screen Resolution: {self.screen_resolution}, Weight: {self.weight} grams"

    def browse_internet(self):
        print(f"Browsing the internet on {self.name}")

    def use_touchscreen(self):
        print(f"Using the touchscreen of {self.name}")
        