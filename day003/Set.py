s_a = set({1, 2, 3, 4, 5, 6, 7, 8, 9})
s_d = set({6, 7, 8, 9, 10, 11})
s_e = set(s_a | s_a)
print("s_a and s_d", s_a and s_d)
print("s_a or s_d", s_a or s_d)
print("s_d and s_a", s_d and s_a)
print("s_d or s_a", s_d or s_a)
print(s_a.intersection(s_d))
print(s_a.difference(s_d))
print(s_d.intersection(s_a))
print(s_d.difference(s_a))
print(s_d - s_a)
print(s_d.union(s_a))
print(s_d | s_a)
print(s_d.symmetric_difference(s_a))
print(s_d ^ s_a)
print(s_d.issubset(s_a))
print(s_e.issubset(s_d))
# list_a = [1, 2, 3, 4, 5, 6]
# s_b = set(list_a)
# s_c = set({"a", "b", "c", "d"})


# print(s_b)
# print(s_a)
# for i in s_a:
#     print(i, end="")
# s_a.update([10])
# print("\n更新", s_a)
# s_a.add(11)
# print("添加", s_a)
# s_a.pop()
# print("出栈", s_a)

