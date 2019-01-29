def word_in_string(word, string):
    starting = len(word)

    if len(word) > len(string):
        return False
    elif word[0:] == string[:starting]:
        return True
    else:
        return word_in_string(word[0:], string[starting:])


print(word_in_string("algorithm", "algorithms are not fun!"))
print(word_in_string("samosas", "Menu: pizza, sandwich"))
print(word_in_string("algorithm", "a nice lgorithm"))
print(word_in_string("", "empty strings are everywhere"))
print(word_in_string("computer", "computer"))
print(word_in_string("pseudocode", ""))
