# Find the sum of elements at even positions in a list
lst = list(map(int, input().split()))
print(sum(lst[i] for i in range(0, len(lst), 2)))
