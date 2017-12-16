import sys
print(sys.getdefaultencoding())
example = "我爱北京天安"
example.encode("GBK")
print(example)
print("gbk", example)
