# program to find the sum of squares of elements in a tuple
tup = tuple(map(int, input("Enter elements : ").split()))
print(sum(x**2 for x in tup))