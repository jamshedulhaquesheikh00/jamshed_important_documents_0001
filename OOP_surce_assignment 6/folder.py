class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor

    def __call__(self, value):
        return value * self.factor  # Make the object callable

# Example usage
m = Multiplier(5)

# Test with callable()
print(callable(m))  # Output: True

# Call the object like a function
result = m(10)
print(result)  # Output: 50
