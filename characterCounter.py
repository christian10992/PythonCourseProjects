def main():
    my_string = ('The quick brown fox jumps over the lazy dog! ' +
                 'But then the lazy dog BITES the fox and then ' +
                 'the fox SCREAMS at the lazy dog. ' +
                 'Now YOU tell me who is at fault?')

    # find number of upper, lower, space, and punctuation chars in string
    counts = findCounts(my_string)

    string_length = len(my_string)
    
    new_string = my_string.replace('lazy', 'hyperactive')

    showResults(my_string, counts, string_length, new_string)

def findCounts(my_string):
    count = 0
    uppercase = 0
    lowercase = 0
    spaces = 0
    punctuation = 0
    for x in my_string:
        if x.isupper() == True:
            uppercase += 1
        elif x.islower() == True:
            lowercase += 1
        elif x.isspace() == True:
            spaces += 1
        else:
            punctuation += 1
        count += 1
    return [uppercase, lowercase, spaces, punctuation]

def showResults(my_string, counts, string_length, new_string):
    print('The original sentence is:', my_string)
    print()
    print('It is', string_length, 'characters long.')
    print('It contans the following characters: ')
    print(counts[0], 'uppercase characters.')
    print(counts[1], 'lowercase characters.')
    print(counts[2], 'spaces')
    print(counts[3], 'punctuation marks.')
    print()
    print('The new sentence is:', new_string)

main()
