lst = [1, 2, 3, 4, 5]   

result = []

middle = (len(lst) + 1) // 2

result.append(lst[:middle])
result.append(lst[middle:])

print(result)
