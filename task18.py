while True:
    a = float(input("Enter the first number: "))
    op = input("Enter the operation (+, -, *, /): ")
    b = float(input("Enter the second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("You can't divide by zero!")
            continue
        result = a / b
    else:
        print("Unknown operation")
        continue

    print("Result:", result)

    answer = input("Continue working? (y/yes): ").lower()

    if answer != "y" and answer != "yes":
        print("Calculator has finished working")
        break
