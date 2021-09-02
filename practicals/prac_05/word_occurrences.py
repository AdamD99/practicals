word_string = input("Text: ")
word_list = word_string.split()
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1


word_list = list(word_count.keys())
word_list.sort()
word_length = max(len(word_list) for word in word_list)
for word in word_list:
    print("{:{}} : {}".format(word, word_length, word_count[word]))
