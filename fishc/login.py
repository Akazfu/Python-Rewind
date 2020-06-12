data = {'mike': 'aaa123'}


def register():
    global data
    user = input('请输入用户名')
    if user not in data.keys():
        password = input('请输入密码')
        data[user] = password
        print('注册成功')
    else:
        print('已经被注册了')


def login():
    global data
    user = input('请输入用户名')
    password = input('请输入密码')
    if data[user] == password:
        print('登入成功')
    else:
        print('密码或用户名错误')


while 1:
    print('''

    --- 新建用户： N/n --- 
    --- 登入账号： E/e --- 
    --- 退出程序： Q/q --- 
    
    ''')
    call = input('请输入指令：')
    if call.upper() == 'N':
        register()
    if call.upper() == 'E':
        login()
    if call.upper() == 'Q':
        break

