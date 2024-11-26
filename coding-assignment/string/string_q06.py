# Remove all characters except alphabets
st = input()
if st == '':
    print('Empty String')
else:
    print(''.join(c for c in st if c.isalpha()))