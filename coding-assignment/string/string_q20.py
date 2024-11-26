# Split String on vowels
st = input()
print(" ".join(word for word in st.split() if not any(char in word for char in "aeiou")))
