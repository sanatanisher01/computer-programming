# Python program to print all even numbers in a range
start = int(input())
end = int(input())
print([i for i in range(start, end) if i % 2 == 0])

