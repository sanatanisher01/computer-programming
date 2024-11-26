# Scraping And Finding Ordered Words In A Dictionary using Python
print("\n=== Find Ordered Words in Dictionary ===")
print("This program will find words where letters are in alphabetical order.")

def is_ordered_word(word):
    """Check if letters in word are in alphabetical order."""
    word = word.lower()
    return list(word) == sorted(word)
print("\nEnter words (one per line, empty line to finish):")
words = []
while True:
    word = input().strip()
    if not word:=
        break
    words.append(word)=
ordered_words = []
for word in words:
    if len(word) > 1 and word.isalpha() and is_ordered_word(word):
        ordered_words.append(word)
print("\n=== Results ===")
print(f"Total words analyzed: {len(words)}")
print(f"Ordered words found: {len(ordered_words)}")
print("\nOrdered words:")
for word in sorted(ordered_words):
    print(f"- {word} ({''.join(sorted(word.lower()))})")