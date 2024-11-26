# program to find the sum of keys in a dictionary
print(sum(dict(zip(input("Enter keys : ").split(), input("Enter values : ").split())).keys()))