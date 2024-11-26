# Odd Frequency Characters
st = input()
print("".join(sorted({char for char in st if st.count(char) % 2 != 0})))

