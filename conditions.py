print("********** Welcome to ABC Bank ATM **********")
print("********** ATM Services **********")

pin = int(input("Enter your ATM PIN: "))

if pin == 1234:
    print("Welcome to ABC Bank")

    balance = 5000

    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your account balance is Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0:
            if amount <= balance:
                balance = balance - amount
                print("Please collect your cash")
                print("Remaining balance: Rs.", balance)
            else:
                print("Insufficient balance")
        else:
            print("Enter a valid amount")

    elif choice == 3:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Money deposited successfully")
            print("Updated balance: Rs.", balance)
        else:
            print("Enter a valid amount")

    elif choice == 4:
        print("Thank you for using ABC Bank ATM")

    else:
        print("Invalid choice")

else:
    print("Incorrect ATM PIN")
    print("Please try again")