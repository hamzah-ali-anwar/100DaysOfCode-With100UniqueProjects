'''Create a program capable of greeting you with Good Morning, Good Afternoon and Good Evening. You program 
should use time module to get the current hour. '''

import time

currentTimeHour = int(time.strftime('%H'))
print(currentTimeHour)

if 4 <= currentTimeHour <= 10:
    print("Good Morning")
elif 11 <= currentTimeHour <= 15:
    print("Good Afternoon")
elif 16 <= currentTimeHour <= 20:
    print("Good Evening")
else:
    print("Good Night")
