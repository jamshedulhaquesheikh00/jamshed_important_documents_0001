class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of Person
        self.subject = subject

    def show_info(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Create a Teacher object
t1 = Teacher("Mr. Smith", "Mathematics")
t1.show_info()
