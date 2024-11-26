# program to check a number is a armstrong number or not
def is_armstrong(n):
    return sum(int(digit)**len(str(n)) for digit in str(n)) == n

print(is_armstrong(int(input())))
