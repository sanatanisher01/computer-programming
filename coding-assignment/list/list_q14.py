# Remove all odd numbers from list
lst = list(map(int, input().split()))
print([i for i in lst if i % 2 == 0])
