file = open("shi", "r", encoding="utf-8")
read_file = file.read()
print(read_file)
file.close()
file = open("shi", "w", encoding="utf-8")
data = read_file+"\n"+"shi"
file.write(data)
file.close()
file = open("shi", "r", encoding="utf-8")
list_file = file.readlines()
for i in list_file:
    print(i.strip())
for i in file:
    print(i)
# file2 = open("zack", "x", encoding="GBK")
# data2 = ""
# file2.write(data2)
