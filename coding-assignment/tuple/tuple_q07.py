# program to find the average of elements in a tuple
tup = tuple(map(int, input().split()))
print(f"Average: {sum(tup) / len(tup)}")