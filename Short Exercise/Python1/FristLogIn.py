user = input("What is your username? ")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print(f"Welcome to the calculator system, user {user}")
    while True:
        print("Options from 1 to 5")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = input("What is your option? (1, 2, 3, 4, 5): ")

        if option == "5":
            print("You exited the calculator")
            break
        if option in ["1", "2", "3", "4"]:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            
            if option == "1":
                print("🔥 The sum is: ", add(number1, number2))
            elif option == "2":
                print("🔥 The subtraction is: ", subtract(number1, number2))
            elif option == "3":
                print("🔥 The multiplication is: ", multiply(number1, number2))
            elif option == "4":
                print("🔥 The division is: ", divide(number1, number2))
        else:
            print("😭 That value is not valid")
         
calculator()
