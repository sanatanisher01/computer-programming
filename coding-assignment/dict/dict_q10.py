# Program to find Maximum record value key in dictionary
print("\n=== Find Key with Maximum Value ===")
print("This program will find the key(s) with the maximum value in a dictionary.")
while True:
    try:
        n = int(input("\nEnter number of dictionary items: "))
        if n > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")
records = {}
print("\nEnter key and value (separated by space)")
print("Example: John 85")

for i in range(n):
    try:
        print(f"\nRecord {i+1}:")
        key, value = input("Enter: ").split()
        records[key] = float(value)
    except ValueError:
        print("Error: Please enter a key and numeric value separated by space")
        i -= 1
max_value = max(records.values())
max_keys = [key for key, value in records.items() if value == max_value]
print("\n=== Results ===")
print("Dictionary:", records)
print(f"Maximum value: {max_value}")
print("Key(s) with maximum value:", max_keys)