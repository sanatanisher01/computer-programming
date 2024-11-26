# program to capitalize the first letter of each word in a string
def capitalize_first_letter(st):
    return " ".join(word.capitalize() for word in st.split())

print(capitalize_first_letter(input()))
