print("---欢迎来到商店----")
print("1. iphone 5800")
print("2. mac book 9000")
print("3. coffee 32")
print("4. bicycle 1500")
iphone = ["iphone", 5800]
mac = ["macBook", 9000]
coffee = ["coffee", 32]
bicycle = ["bicycle", 1500]
shop = [iphone, mac, coffee, bicycle]
shopCar = []
wallet = 20000
expenditure = 0
while True:
    my = input(">>请输入要买的商品：")
    if my == "q":
        print("退出")
        break
    if 4 >= int(my) >= 1:
        print(shop)
        print("要买的商品", shop[int(my)-1])
        if (shop[int(my)-1])[1] <= wallet:
            shopCar.append(shop.pop(int(my)-1))
            wallet = wallet - (shop[int(my)-1])[1]
            print("您购买了：", shopCar)
            print("余额为：", wallet)
            for i in range(shopCar.__len__()):
                expenditure += shopCar[i][1]
            print("本次消费额为：", expenditure)
        else:
            print("你没有足够的钱购买此商品")
    else:
        print("商店没有您需要的商品")