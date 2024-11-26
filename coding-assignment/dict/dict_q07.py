# Program to replace words in a text using a dictionary
print("\n=== Word Replacement Program ===")
print("This program will help you replace specific words in your text.")
print("\nExample:")
print("If you want to replace 'hello' with 'hi' and 'world' with 'earth'")
print("Input text: 'hello world'")
print("Output will be: 'hi earth'\n")
replacements = {}
while True:
    try:
        n = int(input("\nHow many words do you want to replace? "))
        if n > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")
print("\nEnter each word pair separated by space (original replacement)")
print("Example: hello hi")

for i in range(n):
    try:
        print(f"\nPair {i+1}:")
        original, replacement = input("Enter: ").split()
        replacements[original] = replacement
    except ValueError:
        print("Error: Please enter two words separated by space")
        i -= 1
print("\nYour replacement pairs:")
for original, replacement in replacements.items():
    print(f"'{original}' will be replaced with '{replacement}'")
print("\nNow enter the text where you want to make these replacements")
text = input("Your text: ")
modified_text = text
for old_word, new_word in replacements.items():
    modified_text = modified_text.replace(old_word, new_word)
print("\n=== Results ===")
print("Original text:", text)
print("Modified text:", modified_text)