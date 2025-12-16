lst = [55, 4, 12, 22, 44]  

if len(lst) > 1:
    last = lst[-1]      
    lst = [last] + lst[:-1]  
    
print(lst) 
