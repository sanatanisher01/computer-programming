# Python program to check if a number is a perfect cube
def is_perfect_cube(n):
    return int(n**(1/3))**3 == n

print(is_perfect_cube(int(input())))
