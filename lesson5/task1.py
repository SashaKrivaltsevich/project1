s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(f'!{second_word}! !{first_word}!')
print("!{second_word}! !{first_word}!".format(second_word=second_word, first_word=first_word))

