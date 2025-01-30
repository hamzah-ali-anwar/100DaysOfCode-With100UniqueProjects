'''Create a program capable of greeting you with Good Morning, Good Afternoon and Good Evening. You program 
should use time module to get the current hour. '''

# complete this program using function

import time

def greet():
    local_hour = int(time.strftime('%H'))

    if 4 <= local_hour <= 10:
        return ("Good Morning")
    elif 11 <= local_hour <= 15:
        return ("Good Afternoon")
    elif 16 <= local_hour <= 20:
        return ("Good Evening")
    else:
        return ("Good Night")
    
print(greet())