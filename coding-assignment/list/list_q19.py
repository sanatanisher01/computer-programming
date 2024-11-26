# Python program to print all prime numbers in a range
start = int(input())
end = int(input())
print([i for i in range(start, end) if all(i % j != 0 for j in range(2, i))])
