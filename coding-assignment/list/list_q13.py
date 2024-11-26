# Program to print duplicates from a list of integers
lst = list(map(int, input().split()))
print(sorted({i for i in lst if lst.count(i) > 1}))

