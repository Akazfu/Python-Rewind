def Dec2Bin(dec):
    dec = int(dec)
    list1 = []
    while dec:
        remainder = dec % 2 
        divident = dec // 2
        dec = divident
        list1.append(str(remainder))
    list1.reverse()
    binary_code = ''.join(list1)
    return binary_code

a = input()
print(Dec2Bin(a))

# def Bin(n):
#     temp = ''
#     if n:
#         temp = Bin(n//2)
#         temp += str(n%2)
#         return temp
#     else:
#         return temp        
# num = int(input('请输入一个十进制数：'))
# print(num,'-->',Bin(num))