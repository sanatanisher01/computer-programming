# program to print and count all prime numbers in a range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
start = int(input())
end = int(input())
prime_count = 0
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
        prime_count += 1
print(f"\nTotal prime numbers: {prime_count}")