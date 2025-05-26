# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        super().__init__(message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print("Age is valid.")

# Example usage
try:
    check_age(16)
except InvalidAgeError as e:
    print("Exception caught:", e)

