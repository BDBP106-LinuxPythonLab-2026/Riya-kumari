paragraph = input("Enter a paragraph: ")

word_count = {}

# Split the paragraph into words
words = paragraph.split()

# Count the frequency of each word
for word in words:
    word = word.strip(".,!?;:").lower()

    if word:
        word_count[word] = word_count.get(word, 0) + 1

# Print words alphabetically with their counts
print("\nWord Frequencies:")
for word, count in sorted(word_count.items()):
    print(word, ":", count)

# Find the maximum frequency
if word_count:
    max_count = max(word_count.values())

    print("\nMost Frequent Word(s):")
    for word, count in sorted(word_count.items()):
        if count == max_count:
            print(word, ":", count)

