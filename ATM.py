#Simple ATM program

balance = 1000
correct_pin = "1234"

attempts = 3
while attempts>0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access granted.")
        break
    else:
        attempts-=1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
if attempts==0:
    print("Too many incorrect attempts. Access dennied.")
else:
    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is ${balance}")

        elif choice == "2":
            amount = float(input("Enter deposite amount: $"))
            if amount>0:
                balance+=amount
                print(f"${amount} deposited. \nNew balance: ${balance}")
            else:
                print("Invalid deposite")
        
        elif choice == "3":
            amount = float(input("Enter withdrawl amount: $"))
            if 0 < amount<=balance:
                balance-=amount
                print(f"${amount} withdrawn. \nNew balance: ${balance}")
            else:
                print("Invalid withdrawl ammount or Insufficient balance.")

        elif choice== "4":
            print("Thank You for using the ATM. \nGoodbye!!!")
            break
        else:
            print("Invalid option. Please try again.")




            



























