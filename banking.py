print("********** Welcome to ABC Bank **********")
print("********** Create a New Bank Account **********")

customer_type = input("Are you a new customer or an existing customer? ")

if customer_type == "new":
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to create a bank account")

        account_type = input("Enter account type (savings/current): ")

        if account_type == "savings":
            print("Savings account selected")
            deposit = float(input("Enter initial deposit amount: "))

            if deposit >= 500:
                print("Congratulations! Your account is created")
                print("Customer Name:", name)
                print("Account Type: Savings")
                print("Initial Deposit:", deposit)
                print("Account Status: Active")

            else:
                print("Minimum initial deposit is Rs. 500")

        elif account_type == "current":
            print("Current account selected")
            deposit = float(input("Enter initial deposit amount: "))

            if deposit >= 1000:
                print("Congratulations! Your account is created")
                print("Customer Name:", name)
                print("Account Type: Current")
                print("Initial Deposit:", deposit)
                print("Account Status: Active")

            else:
                print("Minimum initial deposit is Rs. 1000")

        else:
            print("Invalid account type")

    else:
        print("Sorry, you must be at least 18 years old")

elif customer_type == "existing":
    print("Welcome back to ABC Bank")
    print("Please visit the existing account services")

else:
    print("Invalid customer type")
    print("Please enter new or existing")