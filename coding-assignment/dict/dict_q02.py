# Program to find the length of a dictionary
print("\n=== Dictionary Length Calculator ===")
print("This program will help you create a dictionary and find its length.")
while True:
    try:
        n = int(input("\nEnter number of items: "))
        if n > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")
my_dict = {}

print("\nEnter key and value (separated by space)")
print("Example: name John")
for i in range(n):
    try:
        print(f"\nItem {i+1}:")
        key, value = input("Enter: ").split()
        my_dict[key] = value
    except ValueError:
        print("Error: Please enter both key and value separated by space")
        i -= 1
print("\n=== Results ===")
print("Your dictionary:", my_dict)
print(f"Length of dictionary: {len(my_dict)} items")