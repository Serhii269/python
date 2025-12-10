minutes = int(input("Enter the number of minutes:"))
hours = minutes // 60         
remaining_minutes = minutes % 60   
print(hours, "hours", remaining_minutes, "minutes")