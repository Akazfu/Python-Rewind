def findvowel(input_str):
    vowel = set('aeiouAEIOU')
    longest_str = ''
    current_str = ''
    input_str += '#'
    for cha in input_str:
        if cha in vowel:
            current_str += cha
        else:
            if len(current_str) > len(longest_str):
                longest_str = current_str
            current_str = ''
    if longest_str != '':
        print(len(longest_str))
    else:
        print(0)


input_str = 'asdbuioAEdevauufgh'
findvowel(input_str)
