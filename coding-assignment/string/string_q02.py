# Python program to check whether the string is Symmetrical or Palindrome
st = input()
if st == st[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

length = len(st)

if length % 2 == 0 and st[:length//2] == st[length//2:]:
    print("Symmetrical")
else:
    print("Not Symmetrical")
