# Python program to capitalize the first and last character of each word in a string
st = input()
print(' '.join(word[:-1] + word[-1].upper() for word in st.split()))
