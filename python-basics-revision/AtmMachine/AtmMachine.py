account = {'Balance':1000,'PIN':'2467'}

def display_menu():
    print("\nWelcome to ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice between(1-4):"))
    return choice


def check_balance():
    print(f"Your current balance is ${account['Balance']}")
    
def deposit_money():
    deposit_amount = int(input("Enter the amount you want to deposit:"))
    account['Balance'] += deposit_amount
    print(f'''${deposit_amount} is deposited in your account.
Your new balance is ${account['Balance']}''')
    
def withdraw_money():
    withdraw_amount = int(input("Enter the amount you want to withdraw:"))
    if account['Balance'] > 0:
        if account['Balance'] > withdraw_amount:
            account['Balance'] -= withdraw_amount
            print(f'''${withdraw_amount} has been withdrawn.
Your new balance is ${account['Balance']}''')
    else:
        print("Insufficient amount.")

def atm():
    pin = input("Please Enter your PIN: ")
    if pin == account['PIN']:
        while True:
            choice = display_menu()
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit_money()
            elif choice == 3:
                withdraw_money()
            elif choice == 4:
                print("Thank you for using the ATM. ")
                break
            else:
                print("Invalid Choice, Please select a valid option(1-4).")
    else:
        print("Invalid PIN. Please try again.") 
        
        
atm()