
class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")

# Create a Logger object
log = Logger()

# Manually delete the object to trigger __del__ (optional)
del log
