import LogUtil

# 高级函数
count = 1024


def display_hello(string):
    print(string)


# 不定长参数
def add(*args):
    for arg in args:
        print(arg)


def add(a, b):
    return a + b


def add_height(a, b, func):
    return a + b + func(a, b)


def multiplication(a, b):
    return a * b


def multiplication_height(a, b):
    return add(multiplication(a, b), multiplication(b, a))


def factorial(a):
    b = 1
    for i in range(1, a + 1):
        b = b * i
    return b


# 递归函数
def factorial_high(a):
    if a == 1:
        return 1
    return a * factorial_high(a - 1)


def fibonacci(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        return 1
    return fibonacci(a - 1) + fibonacci(a - 2)


# def fibonacci_high(a):
#     # before = a - 2
#     # after = a - 1
#     result = 0
#     for i in range(a):
#         if i == 0:
#             result = 0
#         elif i == 1 & i == 2:
#             result = 1
#         else:
#             result = (i - 1) + (i - 2)
#         print(result, end=" ")
#     return result


def personal_info(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])
        # LogUtil.print_log(i+"", ""+kwargs[i])


def change_count():
    count = 2048
    print(count)


# add(1, 2, 3, 4, 5, 6)
# display_hello("hello")
# LogUtil.print_log("zack", "content")
# personal_info(name="zack", age=24, height=165)
# change_count()
# print(add(2, 3))
# print(add_height(2, 3, multiplication))
# print(multiplication(2, 3))
# print(multiplication_height(2, 3))
# print(factorial(100))
# print(factorial_high(2))
for i in range(10):
    print(fibonacci(i), end=" ")

# fibonacci_high(10)
