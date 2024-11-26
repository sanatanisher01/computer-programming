# program to find the sum of cubes of elements in a tuple
tup = tuple(map(int, input("Enter elements : ").split()))
print(sum(x**3 for x in tup))