# Create a list of numbers
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Ask the user for a number to search
target = int(input("Enter a number to search for: "))

# Perform the linear search
found = False  # Assume the number is not found initially

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True  # Number found
        break

# Print the result
if found:
    print(f"The number {target} is in the list.")
else:
    print(f"The number {target} is not in the list.")
