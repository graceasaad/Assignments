class sandwichMaker:
    def __init__(self):
        self.resources={
            "bread": 12,
            "ham": 18,
            "cheese": 24
        }

        self.recipes = {
            "small": {
                "ingredients": {
                    "bread": 2,
                    "ham": 4,
                    "cheese": 4,
                },
                "cost": 1.75,
            },
            "medium": {
                "ingredients": {
                    "bread": 4,
                    "ham": 6,
                    "cheese": 8,
                },
                "cost": 3.25,
            },
            "large": {
                "ingredients": {
                    "bread": 6,
                    "ham": 8,
                    "cheese": 12,
                },
                "cost": 5.50,
            }
        }


    def check_resources(self, ingredients):
        for item, amount  in ingredients.items():
            if self.resources[item] < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True
    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: "))
        halfs= int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = (dollars * 1.0)+ (halfs* 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, inserted, cost):
        if inserted < cost:
            print ("Sorry thats not enough money, Money refunded.")
            return False
        elif inserted >= cost:
            change = round(inserted - cost, 2)
            print (f"Here is ${change} in change.")
        return True
    def make_sandwich(self, s_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.resources[item]-= amount
        print(f"{s_size} sandwich is ready. Bon appetit!")

    def report(self):
        print(f"Bread: {self.resources['bread']} slice(s)")
        print (f"Ham: {self.resources['ham']} slice(s)")
        print (f"Cheese: {self.resources['cheese']} pounds(s)")
def main():
    machine = sandwichMaker()
    is_on = True
    while is_on:
        choice = input("What would you like? (Small/ Medium/ Large/ Report/ Off): ").lower()

        if choice == "off":
            is_on= False

        elif choice == "report":
            machine.report()

        elif choice in machine.recipes:
            sandwich = machine.recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                payment = machine.process_coins()
                if machine.transaction_result(payment, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



