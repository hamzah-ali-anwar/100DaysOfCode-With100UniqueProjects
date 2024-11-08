def count_letters(names, word):
    combined_names = ''.join(names).upper()
    return sum(combined_names.count(letter) for letter in word.upper())

def calculate_love_percentage(name1, name2):
    # Count occurrences of 'TRUE'
    true_count = count_letters([name1, name2], 'TRUE')
    
    # Count occurrences of 'LOVE'
    love_count = count_letters([name1, name2], 'LOVE')
    
    # Combine the counts
    combined_count = int(str(true_count) + str(love_count))
    
    # Ensure the result is a two-digit number
    if combined_count < 10:
        combined_count *= 10
    elif combined_count > 99:
        combined_count = combined_count % 100
    
    return combined_count

# Get input from user
name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

# Calculate and print the result
result = calculate_love_percentage(name1, name2)
print(f"\nYour love percentage is: {result}%")
