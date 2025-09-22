class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: "))
        halfs = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = (dollars * 1.0) + (halfs * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, inserted, cost):
        if inserted < cost:
            print("Sorry thats not enough money, Money refunded.")
            return False
        elif inserted> cost:
            change = round(inserted - cost, 2)
            print(f"Here is ${change} in change.")
        return True
