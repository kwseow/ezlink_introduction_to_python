def longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if (len(longest_word) < len(word)):
            longest_word = word
    return longest_word

sentence = "You are so close - but I think the problem"
word_list=sentence.split()
print(longest_word(word_list))

