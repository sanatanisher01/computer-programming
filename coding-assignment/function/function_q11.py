# Python program to check if a string is a palindrome
def is_palindrome(st):
    return st == st[::-1]

print(is_palindrome(input()))
