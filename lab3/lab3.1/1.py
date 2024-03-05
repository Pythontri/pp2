class S:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

# Example usage:
s1 = S()
s1.getString()
s1.printString()