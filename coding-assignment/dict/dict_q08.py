# Program to remove duplicate values across Dictionary Values
print("\n=== Remove Duplicate Values from Dictionary ===")
print("This program will remove duplicate values across all dictionary items.")
while True:
    try:
        n = int(input("\nEnter number of dictionary items: "))
        if n > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")
dict_items = {}
print("\nEnter key and values (separated by spaces)")
print("Example: key value1 value2 value3")

for i in range(n):
    try:
        print(f"\nItem {i+1}:")
        entry = input("Enter: ").split()
        if len(entry) < 2:
            print("Error: Please enter at least one key and one value")
            i -= 1
            continue
            
        key = entry[0]
        values = entry[1:]
        dict_items[key] = values
        
    except ValueError:
        print("Error: Invalid input format")
        i -= 1
print("\n=== Original Dictionary ===")
for key, values in dict_items.items():
    print(f"{key}: {values}")
seen_values = set()
unique_dict = {}

for key, values in dict_items.items():
    unique_values = []
    for value in values:
        if value not in seen_values:
            unique_values.append(value)
            seen_values.add(value)
    
    if unique_values:
        unique_dict[key] = unique_values
print("\n=== Dictionary After Removing Duplicates ===")
for key, values in unique_dict.items():
    print(f"{key}: {values}")