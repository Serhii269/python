number_1 = int(input("Enter a nummer: "))
opperation = input("Enter a opperation: ")
number_2 = int(input("Enter another nummer: "))
match opperation:
    case "+":
        result = number_1 + number_2
    case "-":
        result = number_1 - number_2
    case "*":
        result = number_1 * number_2
    case "/":
        result = "You can‘t divide by zero" if number_2 == 0 else number_1 / number_2
    case _:
        result = "Unknown opperation"
print (result)
    
