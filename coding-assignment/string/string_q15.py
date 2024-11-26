# Remove All Duplicates from a Given String in Python
st = input()
print("".join(sorted(set(st), key=st.index)))
