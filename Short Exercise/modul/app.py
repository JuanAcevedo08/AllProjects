import request
import time

def menu():
    options = ["1 - Use calculator", "2 - Exit"]
    while True:
        print("Welcome to the menu, Things to do:")
        time.sleep(1)
        for option in options:
            print("Options", option)
            time.sleep(0.5)

        choice = int(input("What would you like to do today?: "))

        if choice == 1:
            request.calculator_menu()
            view_records = input("Would you like to see the records? \n").lower()
            if view_records == "yes":
                operation = input("Which record would you like to see: ")
                request.operation_log(operation)
                break
            else:
                break
        elif choice == 2:
            print("Exiting...")
            time.sleep(2)
            break
        else:
            break

menu()
