test_worlds = ('mum', 'cat', 'dad', 'dog', 'map', 'level')

def check_palindrome(test_worlds):
    return test_worlds[::-1] == test_worlds

my_filter = tuple(filter( check_palindrome, test_worlds))
print (my_filter)