# x, y, z = 2, 1, 3

# small = x if (x < y and x < z) else (y if y < z else z)
# print(small)

# count = 3
# secret = 11235813
# while count:
#     user_input = input('input')
#     if user_input == secret:
#         print('loged in')
#         break
#     elif '*' in user_input:
#         print('wrong code')
#     else:
#         print('wrong code')
#         count -= 1

# for i in range(100, 1000):
#     a = i // 100
#     b = i // 10 - a * 10
#     c = i - a * 100 - b * 10

#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)

# for i in range(100, 1000):  
#     sum = 0  
#     temp = i  
#     while temp:  
#         sum = sum + (temp%10) ** 3  
#         temp //= 10           
#     if sum == i:  
#         print(i) 

for r in range(4):
    for y in range(4):
        for g in range(2,7):
            if r + y + g == 8:
                print('outcome: '+r*'r'+y*'y'+g*'g')