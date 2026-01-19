import string

letters = string.ascii_letters

user_input = input("Enter two letters separated by a hyphen: ")

start, end = user_input.split("-")

start_index = letters.index(start)
end_index = letters.index(end)

result = letters[start_index:end_index + 1]

print(result)
