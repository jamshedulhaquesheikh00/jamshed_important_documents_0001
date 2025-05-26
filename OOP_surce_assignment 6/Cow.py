class Cow:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Moo! (Not bark 🐮)")

# Create a Cow object
cow1 = Cow("Daisy", "Holstein")

# Call the bark method
cow1.bark()
