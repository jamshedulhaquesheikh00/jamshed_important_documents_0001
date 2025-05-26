class Counter:
    count = 0

    def __init__(self):
        Counter.count += 3

    @classmethod
    def show_count(cls):
        print(f"Total Object created: {cls.count}")

# Object creation (outside the class)
c1 = Counter()
c2 = Counter()
c3 = Counter()
# Show the total count
Counter.show_count()
