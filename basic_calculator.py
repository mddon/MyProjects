def basic_calculator():
    print("Welcome to Mimz basic calculator! Perform simple task between two numbers")
    while True:
        try:
            num1 = float(input("\nEnter your first number: "))
            num2 = float(input("Enter your second number: "))
            math_operation = input("Enter the math operation you want to perform: (-, +, *, /): ")

            if math_operation not in ["+", "-", "*", "/"]:
                print("Invalid operation! Please choose from: (-, +, *, /)")
                continue

            if math_operation == "/" and num2 == 0:
                print("Error: You can not divide by zero,")
                continue

            if math_operation == "-":
                result = num1 - num2
                result = round(result, 2)
            elif math_operation == "+":
                result = num1 + num2
                result = round(result, 2)
            elif math_operation == "*":
                result = num1 * num2
                result = round(result, 2)
            else:
                result = num1 / num2
                result = round(result, 2)

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


basic_calculator()
