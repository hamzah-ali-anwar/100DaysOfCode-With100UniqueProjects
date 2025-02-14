import math
# Print "Hello, PCEP!" to the console.
print("Hello, PCEP!")

# Assign the value 42 to a variable and print it.
num = 42
print(num)

# Convert the string "123" into an integer and multiply it by 2.
my_string = int("123")
sum = my_string * 2
print(sum)

# Another way of doing it
my_string = "123"
convert_string_to_int = int(my_string)
sum = convert_string_to_int + 4
print(sum)

# Check the type of 3.14 using type().
check_type = type(3.14)
print(check_type)

# Perform integer division of 25 by 4.
integer_division = 25 // 4
print(integer_division)

# Find the remainder when 17 is divided by 5.
reminder = 17 % 5
print(reminder)

# Swap two variables without using a third variable.
swap_one = "first variable"
swap_two = "second variable"

print("Before Swap")
print(swap_one)
print(swap_two)

# Tuple packing, unpacking
swap_one, swap_two = swap_two, swap_one

print("After Swap")
print(swap_one)
print(swap_two)

# Convert a float 3.7 to an integer and explain the result.
'''since task is to just convert float into an int, i used int()
function which truncates the decimal part of the number.
We can use different rounding methods, such as: math.floor(),
math.ceil(), and round() for difference purposes '''

convert_float_to_int = int(3.7)
print(convert_float_to_int)

# math.floor() - rounds down to the nearest integer
convert_float_to_int = 3.7
new_value = math.floor(convert_float_to_int)
print(new_value)

# math.ceil() - rounds up to the nearest integer
convert_float_to_int = 3.7
new_value = math.ceil(convert_float_to_int)
print(new_value)

# round() - rounds to the nearest integer
convert_float_to_int = 3.7
new_value = round(convert_float_to_int)
print(new_value)


