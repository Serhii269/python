seconds = int(input("Enter the number of seconds: "))

seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60

days = seconds // seconds_in_day
seconds = seconds % seconds_in_day

hours = seconds // seconds_in_hour
seconds = seconds % seconds_in_hour

minutes = seconds // seconds_in_minute
seconds = seconds % seconds_in_minute

secs = seconds

if days == 1:
    day_word = "day"
elif 2 <= days <= 4:
    day_word = "days"
else:
    day_word = "days"

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
secs = str(secs).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{secs}")
