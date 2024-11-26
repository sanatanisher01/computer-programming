# Python program to check if a number is a perfect square
def is_perfect_square(n):
    return int(n**0.5)**2 == n

print(is_perfect_square(int(input())))
