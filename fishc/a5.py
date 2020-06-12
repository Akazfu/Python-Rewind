year = int(input('input the year: '))

if year % 4 == 0 and year % 100 != 0 \
        or year % 400 == 0:
    print('今年是闰年。')
else:
    print('今年是平年')
