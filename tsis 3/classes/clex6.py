class Up:
    def __init__(s):
        s.string = ""

    def getString(s):
        s.string = input("write a string: ")

    def printString(s):
        print("Your string in upper case: ", s.string.upper())
funcup = Up()
funcup.getString()
funcup.printString()