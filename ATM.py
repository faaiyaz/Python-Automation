account = {
    "balance": 10000 
}
while True:
    try:
        a = int(input("1. Check balance.\n2. Deposit.\n3. Withdraw.\n4. Exit.\nEnter:"))
        if a == 1:
            print("Here is your balance:", account["balance"])
        elif a == 2:
            b = int(input("Enter amount:"))
            account["balance"] = account["balance"] + b
            print("Here is your new balance:", account["balance"])
        elif a == 3:
            c = int(input("Enter amount:"))
            if c > account["balance"]:
                print("Insufficient balance")
            else:
                account["balance"] = account["balance"] - c
                print("Here is your new balance:", account["balance"])
        elif a == "4":
            print("Have a nice day!")
            break
        else:
            print("kindly choose between 1 - 4")
    except ValueError:
        print("Kindly Choose numbers")