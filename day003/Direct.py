# 字典

direct_a = {"name": "zack", "age": 18}
print(direct_a)
value_a = direct_a.setdefault('email', "shiqizhenyes@163.com")
value_b = direct_a.setdefault('age', 20)
print(direct_a)
print("value_a", value_a)
print("value_b", value_b)
print("name", direct_a.get("name"))
print("name", direct_a["name"])
print("keys", direct_a.keys())
print("values", direct_a.values())
print("items", direct_a.items())
direct_a["name"] = "json"
print(direct_a)
direct_b = {"phone": 18141901466}
direct_a.update(direct_b)
print(direct_a)
print(direct_b)
direct_a.pop("name")
print(direct_a)
del direct_a["age"]
print(direct_a)
# direct_c = dict.fromkeys("name", "age", "phone")
# print("direct_c", direct_c)
direct_a.clear()
print(direct_a)


