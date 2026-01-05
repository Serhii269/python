import random

lst = []

length = random.randint(3, 10)

for i in range(length):
    lst.append(random.randint(1, 9))
    
result = [
    lst[0], 
    lst[2],    
    lst[-2]     
]

print(lst)
print(result)
