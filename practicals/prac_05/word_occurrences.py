word_string = input("Text: ")
word_list = word_string.split()
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1


word_list = list(word_count.keys())
word_list.sort()
for word in word_list:
    print("{} : {}".format(word, word_count[word]))
