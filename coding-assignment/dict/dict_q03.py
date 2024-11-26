# program to find the sum of values in a dictionary
print(sum(dict(zip(input("Enter keys : ").split(), input("Enter values : ").split())).values()))