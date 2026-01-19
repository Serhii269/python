number = int(input("Enter an integer: "))

while number > 9:
    digits = [int(d) for d in str(number)]  
    product = 1
    for d in digits:
        product *= d
    number = product  

print(number)
