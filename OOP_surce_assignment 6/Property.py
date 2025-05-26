class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)
print(p.price)     # Get price
p.price = 150      # Set price
print(p.price)
del p.price        # Delete price
