# 1、函数的定义
"""
   def 函数名(传入参数):
      函数体
      return 返回值
"""


# 2、函数的调用
# 函数名(参数)


# 3、变量的作用域
num = 200
def add():
    # 将函数内部的局部变量变成全局变量
    global num
    num = 100
    print(f"这个变量值是{num}")  # 这个变量值是100(就近原则)

add()
print(num)  # 这个变量值是100


# 4、函数的返回值
def add(a, b):
    result = a + b
    return result

r = add(2, 3)
print(r)

# 4、函数的说明文档
def add2(a, b):
    """
    函数说明
    :param a:形参1
    :param b:形参2
    :return: 返回两个形参相加的最终和
    """
    result = a + b
    return result
print(add2(4, 6))


# 函数的嵌套
def def_a():
    print("----2----")

def def_b():
    print("----1----")
    # 调用def_a函数
    def_a()
    print("----3----")
def_b()


"""
   函数的注意事项：
    1.参数如果不需要，可以省略
    2.返回值如果不需要，可以省略
    3.函数必须先定义，在调用
    4.函数碰到return之后的代码将不再执行
"""