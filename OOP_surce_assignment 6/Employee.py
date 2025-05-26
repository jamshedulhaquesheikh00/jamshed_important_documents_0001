class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected (by convention)
        self.__ssn = ssn          # Private (name mangled)

# Create an object
emp = Employee("Alice", 70000, "123-45-6789")

# Accessing the variables
print("Name:", emp.name)         # ✅ Public - accessible

print("Salary:", emp._salary)    # ⚠️ Protected - accessible, but discouraged

# Try accessing the private variable directly
try:
    print("SSN:", emp.__ssn)     # ❌ Will raise an AttributeError
except AttributeError as e:
    print("Cannot access __ssn directly:", e)

# Access private variable using name mangling
print("SSN (via name mangling):", emp._Employee__ssn)  # ✅ Works, but not recommended
