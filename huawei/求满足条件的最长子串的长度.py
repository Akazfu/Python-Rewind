input_str = "a5"
left = 0
right = 1
length = right - left + 1
max_length = length

if len(input_str) < 2:
    print(-1)
elif input_str.isalpha() or input_str.isnumeric() or not input_str.isalnum():
    print(-1)
last = False
while right != len(input_str) and left <= right:
    if input_str[left].isalpha() and input_str[right].isalpha():
        left += 1
        right += 1
        last = True
    elif input_str[left].isalpha() and input_str[right].isdigit():
        length = right - left + 1
        max_length = max(length, max_length)
        right += 1
        last = False
    elif input_str[left].isdigit() and input_str[right].isdigit():
        length = right - left + 1
        max_length = max(length, max_length)
        right += 1
        last = False
    elif input_str[left].isdigit() and input_str[right].isalpha():
        if last:
            left = right
            right += 1
        else:
            length = right - left + 1
            right += 1
            max_length = max(length, max_length)
        last = True
print(max_length)
