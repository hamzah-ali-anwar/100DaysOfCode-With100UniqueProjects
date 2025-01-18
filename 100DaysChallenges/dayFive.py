import time

local_hour = int(time.strftime('%H'))
print(local_hour)

if  5 <= local_hour < 12:
    print("Good Morning")
elif 12 <= local_hour < 17:
    print("Good Afternoon")
elif 17 <= local_hour < 21:
    print("Good Evening")
else:
    print("Good Night")