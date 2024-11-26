#  Uppercase Half String
st = input()
length = len(st)
if length % 2 == 0:
    print(st[:length//2].upper() + st[length//2:].lower())
else:
    print(st[:length//2+1].upper() + st[length//2+1:].lower())
