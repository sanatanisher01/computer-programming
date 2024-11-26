# Find the sum of elements at odd positions in a list
lst = list(map(int, input().split()))
print(sum(lst[i] for i in range(1, len(lst), 2)))
