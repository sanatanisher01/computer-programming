# Python program to print all palindromes in a range
start = int(input())
end = int(input())
print([i for i in range(start, end) if str(i) == str(i)[::-1]])
