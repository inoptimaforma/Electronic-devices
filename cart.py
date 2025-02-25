class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            print(f"Added {amount} {device.name}(s) to the cart.")
        else:
            print(f"Not enough devices for {device.name}.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if item[1] >= amount:
                    self.items.remove((device, amount))
                    self.total_price -= device.price * amount
                    print(f"Removed {amount} {device.name}(s) from the cart.")
                else:
                    print(f"Cannot remove {amount} {device.name}(s). Only {item[1]} in cart.")
                return
        print(f"{device.name} not found in cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Cart Items:")
            for device, amount in self.items:
                print(f"{device.name} - {amount} unit(s) - ${device.price * amount}")

    def checkout(self):
        if not self.items:
            print("Cart is empty. Nothing to checkout.")
            return

        for device, amount in self.items:
            if not device.is_available(amount):
                print(f"Not enough devices for {device.name}.")
                return
            device.reduce_stock(amount)
        print(f"Total Price: ${self.total_price}")
        print("Thank you for your purchase!")
        self.items = []
        self.total_price = 0