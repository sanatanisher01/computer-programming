# program to check if a number is a perfect number
def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

print(is_perfect_number(int(input())))
