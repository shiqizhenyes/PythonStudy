if __name__ == '__main__':
    msg = "我爱北京天安门"
    print(msg)
    name = input("输入用户名\n")
    passWord = input("输入密码\n")
    print(name)
    print(passWord)
    age = input("输入的你年龄\n")
    if int(age) > 100:
        print("你活了" + age + "年，你成神了")
    else:
        print("你活了" + age + "岁")


