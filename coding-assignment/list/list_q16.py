# Remove all duplicates from a list
lst = list(map(int, input().split()))
print(list(dict.fromkeys(lst)))
