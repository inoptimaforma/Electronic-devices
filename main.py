if __name__ == "__main__":
    devices = [
        Smartphone("iPhone 16 Pro Max", 999, 4, 24, 6.9, 33),
        Laptop("MacBook Air", 1639, 3, 12, 13.6, 3.1),
        Tablet("iPad Pro 11", 1539, 7, 12, 11, 586)
    ]

    cart = Cart()

    while True:
        print("Menu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Devices:")
            for i, device in enumerate(devices):
                print(f"{i + 1}. {device}")
            device_choice = int(input("Enter the device number: ")) - 1
            amount = int(input("Enter the quantity: "))
            cart.add_device(devices[device_choice], amount)

        elif choice == "2":
            cart.print_items()
            print(f"Total price: ${cart.get_total_price()}")
            checkout_choice = input("Do you want to checkout? (yes/no): ").lower()
            if checkout_choice == "yes":
                cart.checkout()

        elif choice == "3":
            break

        