lst = [0, 1, 7, 2, 4, 3, 12, 13, 77]   

if len(lst) == 0:
    result = 0
else:
    s = 0
    for i in range(0, len(lst), 2):
        s += lst[i]

    result = s * lst[-1]

print(result)
