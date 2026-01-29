import string
import keyword

name = input("Enter a variable name: ")

result = True

if name[0].isdigit():
    result = False

if name != name.lower():
    result = False

if " " in name:
    result = False

for symbol in name:
    if symbol in string.punctuation and symbol != "_":
        result = False

if name.strip("_") == "" and name.count("_") > 1:
    result = False

if name in keyword.kwlist:
    result = False

print(result)
