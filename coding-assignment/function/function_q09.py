# Python program to check if a number is a perfect power of k
def is_perfect_power_of_k(n, k):
    return int(n**(1/k))**k == n

print(is_perfect_power_of_k(int(input()), int(input())))
