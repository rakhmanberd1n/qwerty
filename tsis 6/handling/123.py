with open('numbers.txt', 'r') as file:
    # Read the number from the file
    number = int(file.readline())
    # Print the number
    print("The number read from the file is:", number)