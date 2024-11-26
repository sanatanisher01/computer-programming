# Check if a string contains any special character
st = input()
print(any(not c.isalnum() for c in st))
