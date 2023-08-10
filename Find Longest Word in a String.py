def longest_word_in(sentence):
    length=''
    longest_word= sentence.split(' ')
    for word in longest_word:
        if len(word)>len(length):
            length = word
        return length

print(longest_word_in('Hallooooooooo i am anas'))
