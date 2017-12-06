class ShoppingCart:
    def __init__(self):
        self.items = []
    # Adding items in above list
    def add_items(self, it):
        self.items.append(it)

    def __iter__(self):
        sorted_items = sorted(self.items, key=lambda i: i.price)
        return sorted_items.__iter__()


class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Testing
cart = ShoppingCart()
cart.add_items(CartItem('Iphobe', 900))
cart.add_items(CartItem("guitar", 799))
cart.add_items(CartItem("cd", 19))

# What if we want to print in the statement
for item in cart:
  print(" * {} ${}".format(item.name, item.price))
# its not iterable
