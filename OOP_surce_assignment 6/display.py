class A:
    def show(self):
        print("A.show() called")

class B(A):
    def show(self):
        print("B.show() called")

class C(A):
    def show(self):
        print("C.show() called")

class D(B, C):  # Multiple inheritance from B and C
    pass

# Example usage
d = D()
d.show()  # This will follow Python's MRO
print(D.__mro__)  # Display the method resolution order
