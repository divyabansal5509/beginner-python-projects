while True:

    print("\nChoose an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    # Exit condition
    if choice == "7":
        print("Thank you for using the calculator!")
        break

    # Check valid operation
    if choice in ["1", "2", "3", "4", "5", "6"]:

        # Taking inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Addition
        if choice == "1":
            result = num1 + num2
            print("Result =", result)

        # Subtraction
        elif choice == "2":
            result = num1 - num2
            print("Result =", result)

        # Multiplication
        elif choice == "3":
            result = num1 * num2
            print("Result =", result)

        # Division
        elif choice == "4":

            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                result = num1 / num2
                print("Result =", result)
        # Power
        elif choice == "5":
            result = num1 ** num2
            print("Result =", result)

        # Modulus
        elif choice == "6":
            result = num1 % num2
            print("Result =", result)

    # Invalid choice
    else:
        print("Invalid choice! Please select between 1 to 7.")