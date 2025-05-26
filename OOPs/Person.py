# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.state = "Idle"

#     def running(self):
#         self.state = "Running"
#         print(f"{self.name} is now running")
    
#     def walking(self):
#         self.state = "Walking"
#         print(f"{self.state} is now walking")

#     def sleeping(self):
#         print(f"{self.state} is now sleeping")

#     def show_state(self):
#         print(f"{self.name} is currently in '{self.state}' state.")

#     Person = Person("Ali")
#     Person.show_state()

#     Person = walking()
#     Person.show_state()

#     Person = sleeping()
#     Person.show_state()

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.state = "Idle"  # Better default than "Ali"

#     def running(self):
#         self.state = "Running"
#         print(f"{self.name} is now running.")

#     def walking(self):
#         self.state = "Walking"
#         print(f"{self.name} is now walking.")

#     def sleeping(self):
#         self.state = "Sleeping"
#         print(f"{self.name} is now sleeping.")

#     def show_state(self):
#         print(f"{self.name} is currently in '{self.state}' state.")


# # Creating an instance and using the methods
# person = Person("Ali")
# person.show_state()

# person.walking()
# person.show_state()

# person.sleeping()
# person.show_state()

#Parameterized Constructors

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Create an object using the parameterized constructor
person = Person("Ali", 30, "Muckdoom Balaver R240 in Pakistan")

print("Name    :", person.name)     # Output: Ali
print("Age     :", person.age)      # Output: 30
print("Address :", person.address)  # Output: Muckdoom Balaver R240 in Pakistan

