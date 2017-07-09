#switch first two letters and concat to the last
pyg = 'ay'
original = raw_input('what is your name')
if len(original) > 0 and original.isalpha():
    word = original.lower();
    first = word[0]
    s = word + first + pyg
    new_word = s[1:len(new_word)]
    print new_word
else:
    print 'empty'