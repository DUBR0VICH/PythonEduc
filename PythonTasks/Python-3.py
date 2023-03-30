text = input("Введите текст: ")
words = text.split()
word_count = {}

for word in words:
    word = word.strip(".,?!")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common_word = ""
most_common_count = 0

longest_word = ""
longest_length = 0

for word, count in word_count.items():
    if count > most_common_count:
        most_common_count = count
        most_common_word = word
    if len(word) > longest_length:
        longest_length = len(word)
        longest_word = word

print("Наиболее часто встречающееся слово:", most_common_word)
print("Самое длинное слово:", longest_word)
