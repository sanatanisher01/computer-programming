# program to check if a number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(int(input())))
