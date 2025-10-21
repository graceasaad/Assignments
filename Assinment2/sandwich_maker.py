class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.resources[item] < amount:
                print(f"There isn't enough {item}.")
                return False
        return True
    def make_sandwich(self, s_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.resources[item]-= amount
            print("Order complete. Enjoy!")

    def report(self):
        print(f"Bread has {self.resources['bread']} slices left.")
        print(f"Ham has {self.resources['ham']} slices left.")
        print(f"Cheese has {self.resources['cheese']} slices left.")