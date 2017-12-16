if __name__ == '__main__':
    print("欢迎使用计算器\n")
    print("1、四则运算\n")
    print("2、比大小\n")
    calculate = input("选择功能:\n>>")
    if calculate == "1":
        number1 = input("第一个数:>>")
        number2 = input("第二个数:>>")
        cc = input("运算符:>>")
        if cc == "+":
            print("两数之和为:" + int(number1) + int(number2))
    else:
        number1 = input("第一个数:>>")
        number2 = input("第二个数:>>")
        max_num = 0
        if number1 > number2:
            max_num = number1
        else:
            max_num = number2
    print("最大的数为:>>" + max_num)
