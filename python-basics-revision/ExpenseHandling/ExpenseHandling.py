expenses=[]

def add_expense():
    name = input("Enter the expense name: ")
    try:
        amount=int(input("Enter the amount: "))
        #Store in dictionary
        expenses.append({"name": name,"amount": amount})
        print(f"Added: {name} - ${amount}")
    except ValueError:
        print("Invalid input, Please enter a valid expense amount.")

def view_expense():
    if not expenses:
        print("\n No expenses recorded yet.")
        return
    print("\n ----Your Expense ----")
    for index,item in enumerate(expenses,1):
        print(f"{index}. {item['name']}: {item['amount']}")
        
def show_total():
    total = sum(item['amount'] for item in expenses)
    print(f"\nTotal Spending: ${total}")
    
def main():
    while True:
        print("\n1. Add Expense \n2. View Expense \n3. Show Total Expense \n4. Exit")
        choice= int(input("Enter your choice(1-4): "))
        
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            show_total()
        elif choice == 4:
            print("Exiting Tracker!")
            break
        else:
            print("Invalid choice, Please choose correct choice.")
            
if __name__ == "__main__":
    main()
            
            
        