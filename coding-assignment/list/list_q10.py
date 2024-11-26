# Find the sum of squares of elements in a list
lst = list(map(int, input().split()))
print(sum(i**2 for i in lst))
