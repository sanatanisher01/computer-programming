# Find words which are greater than given length k
st = input()
k = int(input())
print([word for word in st.split() if len(word) > k])
