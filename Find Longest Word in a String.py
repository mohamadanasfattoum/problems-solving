'''
def longest_word_in(sentence):
    longest=''
    longest_word= sentence.split(' ')
    for word in longest_word:
        if len(word)>len(longest):
            longest = word
        return longest

print(longest_word_in('Hallooooooooo i am anas'))
'''
def longest_word_in(sentence):
    count = 0
    longest_word= sentence.split(' ')
    for word in longest_word:
        if len(word)>count:
            count = len(word) 
            longest = word
        return longest

print(longest_word_in('Hallooooooooo i am anas'))