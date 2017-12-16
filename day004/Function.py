import LogUtil

count = 1024


def display_hello(string):
    print(string)


# 不定长参数
def add(*args):
    for arg in args:
        print(arg)


def personal_info(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])
        # LogUtil.print_log(i+"", ""+kwargs[i])


def change_count():
    count = 2048
    print(count)


add(1, 2, 3, 4, 5, 6)
display_hello("hello")
# LogUtil.print_log("zack", "content")
personal_info(name="zack", age=24, height=165)
change_count()