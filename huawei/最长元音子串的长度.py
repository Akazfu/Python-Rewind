input_str = 'asdbuiodevauufgh'
vowel = set('aeiouAEIOU')
longest = 0
current = 0
input_str += '$'
for cha in input_str:
    if cha in vowel:
        current += 1
    else:
        if current > longest:
            longest = current
        current = 0
if longest != 0:
    print(longest)
else:
    print(0)
