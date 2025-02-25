class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"Laptop: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months, RAM: {self.ram_size} GB, Processor Speed: {self.processor_speed} GHz"

    def run_program(self):
        print(f"Running a program on {self.name}")

    def use_keyboard(self):
        print(f"Typing on the keyboard of {self.name}")