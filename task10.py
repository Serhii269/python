lst = [1]  

if len(lst) == 0:
    result = [[], []]
else:
    middle = (len(lst) + 1) // 2
    first_half = lst[:middle]
    second_half = lst[middle:]
    result = [first_half, second_half]

print(result)
