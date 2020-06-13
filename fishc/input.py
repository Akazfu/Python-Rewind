while 1:
    usr = input('请输入一个整数：')
    try:
        usrint = int(usr)
        break
    except:
        print('出错，您输入的不是整数')
