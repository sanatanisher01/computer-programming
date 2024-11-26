# program to check if a number is a prime number
def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_prime(int(input())))
