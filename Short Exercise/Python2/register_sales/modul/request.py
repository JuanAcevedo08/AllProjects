import time
import calculator

log = {}

def calculator_menu():
    print("Welcome to the calculator")
    time.sleep(1.5)
    while True:
        sum_count = 0
        subtract_count = 0
        multiply_count = 0
        divide_count = 0
        print("What would you like to do today?")
        time.sleep(0.5)
        print("1. Add")
        time.sleep(0.3)
        print("2. Subtract")
        time.sleep(0.3)
        print("3. Multiply")
        time.sleep(0.3)
        print("4. Divide")
        time.sleep(0.3)
        print("5. Exit")

        option = int(input("What is your choice?: "))

        if option in [1, 2, 3, 4]:
            if option == 1:
                number1 = int(input("Enter the first number to add: "))
                time.sleep(0.2)
                number2 = int(input("Enter the second number to add: "))
                print("Calculating...")
                time.sleep(2)
                print("Result: ", calculator.add(number1, number2))
                sum_count += 1
                time.sleep(0.2)
                exit_or_continue = input("Do you want continue?: ").lower()
                if exit_or_continue == "yes":
                    pass
                else:
                    print("Exiting...")
                    time.sleep(3)
                    print("Exited successfully")
                    break

            elif option == 2:
                number1 = int(input("Enter the first number to subtract: "))
                time.sleep(0.2)
                number2 = int(input("Enter the second number to subtract: "))
                print("Calculating...")
                time.sleep(2)
                print("Result: ", calculator.subtract(number1, number2))
                subtract_count += 1
                time.sleep(0.2)
                exit_or_continue = input("Do you want to exit or continue? Type yes or no: ").lower()
                if exit_or_continue == "yes":
                    pass
                else:
                    print("Exiting...")
                    time.sleep(3)
                    print("Exited successfully")
                    break

            elif option == 3:
                number1 = int(input("Enter the first number to multiply: "))
                time.sleep(0.2)
                number2 = int(input("Enter the second number to multiply: "))
                print("Calculating...")
                time.sleep(2)
                print("Result: ", calculator.multiply(number1, number2))
                multiply_count += 1
                time.sleep(0.2)
                exit_or_continue = input("Do you want to exit or continue? Type yes or no: ").lower()
                if exit_or_continue == "yes":
                    pass
                else:
                    print("Exiting...")
                    time.sleep(3)
                    print("Exited successfully")
                    break

            elif option == 4:
                number1 = int(input("Enter the first number to divide: "))
                time.sleep(0.2)
                number2 = int(input("Enter the second number to divide: "))
                print("Calculating...")
                time.sleep(2)
                print("Result: ", calculator.divide(number1, number2))
                divide_count += 1
                time.sleep(0.2)
                exit_or_continue = input("Do you want to exit or continue? Type yes or no: ").lower()
                if exit_or_continue == "yes":
                    pass
                else:
                    print("Exiting...")
                    time.sleep(3)
                    print("Exited successfully")
                    break

        elif option == 5:
            print("Exiting the program...")
            time.sleep(2)
            print("See you next time!")
            time.sleep(1)
            break

        else:
            print("We don't have that option, sorry.")
            time.sleep(2)
            retry = input("Do you want to try again? Type yes or no: ").lower()
            if retry == "yes":
                return calculator_menu()
            elif retry == "no":
                print("Exiting...")
                time.sleep(0.4)
                print("GOODBYE")
                break

    log["add"] = sum_count
    log["subtract"] = subtract_count
    log["multiply"] = multiply_count
    log["divide"] = divide_count
    
def operation_log(operation):
    if operation in log.keys():
       print(f"Number of times the operation {operation} was performed: ", log[operation])
        

if __name__ == '__main__':
    calculator_menu()
    operation_log()
