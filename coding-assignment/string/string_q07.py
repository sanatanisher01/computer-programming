# Python program to print even length words in a string
st = input().split()
for word in st:
    if len(word) % 2 == 0:
        print(word)
    else:
        continue
