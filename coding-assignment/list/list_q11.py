# Find the sum of cubes of elements in a list
lst = list(map(int, input().split()))
print(sum(i**3 for i in lst))
