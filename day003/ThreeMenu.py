Menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                'CICC': {},
                'HP': {},
                'CCTV': {}
            }
        },
        '昌平': {
            '沙河': {},
            '吉利大学': {},
            '天通苑': {},
            '回龙观': {}
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                '快手': {},
            },
            '中关村': {
                '汽车之家': {},
                '新东方': {}
            }
        }
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                'CICC': {},
                '高盛': {}
            },
            '外滩': {}

        },
        '闵行': {},
        '静安': {}
    },
    '山东': {
        '济南': {},
        '德州': {
            '乐陵': {
                '丁坞镇': {},
                '城区': {}
            },
            '平原': {},
        },
        '青岛': {}
    }
}
currentLayer = Menu
previousLayer = Menu
previousLayers = []
# while True:
#     for k in Menu:
#         print(k)
#     city = input(">>choose:")
#     if city in Menu:
#         for a in Menu[k]:
#             print(a)
#         area = input(">>choose:")
#         if area in Menu[city]:
#             for b in Menu[city][area]:
#                 print(b)
#         town = input(">>choose:")
while True:
    for K in currentLayer:
        print(K)
    choose = input(">>choose:").strip()
    if len(choose) == 0:
        continue
    if choose in currentLayer:
        previousLayers.append(currentLayer)
        currentLayer = currentLayer[choose]
    elif choose == "p":
        if previousLayers:
            currentLayer = previousLayers.pop()
        else:
            print("没有此选项")
    else:
        print("没有此选项")