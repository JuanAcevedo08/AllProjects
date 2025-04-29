AvailableInfo = {
    "Products": {"Hygiene": "Quantity: 30", "Refrigerated Food": "Quantity: 80", "Snacks": "Quantity: 120"},
    "Employees": {"Names and Positions": {"Juan": "SoftwareDev", "Luisa": "Cashier", "Maria": "Administrator", "Valentina": "Marketing", "Laura": "Manager"}},
    "Expenses": {"Company Member Payments": "$200000", "Product Purchases": "$7000", "General Maintenance": "$4000"}
}
print("Welcome to the MarketJuan Navigation System by JuanCRACKPROSUPERPRO", end=" ")
print("What would you like to search for today? Options: ")
MainKeys = AvailableInfo.keys()
print(MainKeys)
Request = input("What would you like to consult today? ")
print(AvailableInfo[Request])