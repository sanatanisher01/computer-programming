#  Program to Accept the Strings Which Contains all Vowels
st = input()
vowels = "aeiou"
print(all(char in st for char in vowels))

