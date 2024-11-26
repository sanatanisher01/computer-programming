# Count the Number of matching characters in a pair of string
st1 = input()
st2 = input()
print(sum(1 for char in st1 if char in st2))

