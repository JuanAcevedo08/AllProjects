def login():
    user = str(input("What is your username: "))
    pw = str(input("What is your password?: "))
    dates = pw
    print("Analyzing data")
    if dates == pw:
        print(f"Welcome to the System, {user}")
    else:
        print("We couldn't recognize the data, please check your username or password")

def nav():
    login()
    while True:
        print("What would you like to check today?")
        print("Options: ")
        print("1. Check Product List")
        print("2. Check Employee List")
        print("3. Check Expense List")
        print("4. Exit Menu")

        option = input("What is your option from 1 to 4?")

        if option == "4":
            print("Exiting the Console, Thank you for visiting")
            break
        elif option in ["1", "2", "3"]:
            if option == "1":
                print("Coming Soon")
            elif option == "2":
                print("Coming Soon")
            else:
                print("Coming Soon")

print(nav())