def count_word_frequencies(text):
    word_freq = {}
    words = text.split()

    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

text = input("Enter the text: ")
word_freq = count_word_frequencies(text)
print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
