def calculator():
    print("Welcome to Mimz calculator! Perform your mathematical task between two numbers")
    while True:
        try:
            num1 = float(input("\nEnter your first number: "))
            num2 = float(input("Enter your second number: "))
            math_operation = input("Enter the math operation you want to perform: (-, +, *, /, exp, mod): ")

            if math_operation not in ["+", "-", "*", "/", "exp", "mod"]:
                print("Invalid operation! Please choose from: (-, +, *, /, exp, or mod)")
                continue

            if math_operation == "/" and num2 == 0:
                print("Error: You can not divide by zero,")
                continue

            operations = {"+": num1 + num2,
                          "-": num1 - num2,
                          "*": num1 * num2,
                          "/": num1 / num2,
                          "exp": num1 ** num2,
                          "mod": num1 % num2
                          }
            result = operations[math_operation]

            print(f"\nResult: {num1} {math_operation} {num2} = {result}\n")
        except ValueError:
            print("Please enter a valid number")

        more_operations = input("Would you want to perform another operation? (yes/no): ").strip().lower()
        if more_operations == "yes":
            print("\nOk! Lets perform another operation")
            continue
        else:
            print("Goodbye!")
            break


calculator()
