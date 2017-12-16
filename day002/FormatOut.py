import time

nick = input(">>输入姓名:")
email = input(">>输入邮箱:")
date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
msg = '''
-----info of zack-----
nick : %s
email : %s
data : %s
---------end----------
''' % (nick, email, date)
print(msg)

for i in range(2):
    username = input(">>请输入用户名:")
    password = input(">>请输入密码:")
    if username == "zack" and password == "123":
        print("登录成功！")
        break
    else:
        print("登录失败")
else:
    print("验证不通过")




