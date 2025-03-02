# 函数的多返回值
def test_return():
    return 1, "hello", True

x, y, z = test_return()
print(x)
print(y)
print(z)

# 函数多种传参方式
def user_info(name, age, gender):
    print(f"你的姓名是:{name},年龄是{age},性别是{gender}")

# 位置参数
user_info("小明", 18, "男")
# 关键字参数
user_info(name="小红",age=18, gender="女")
user_info(age=18, gender="女", name="潇潇")

# 缺省参数（默认值）默认值统一都在最后,如果给age给默认值，gender不给就会报错
def user_info(name, age, gender="男"):
    print(f"你的姓名是:{name},年龄是{age},性别是{gender}")

user_info("小红", 18)
# 不传入参数的时候使用默认值，传入参数会覆盖默认值0

user_info("小红", 18, "女")

# 不定长传入参数
# 不定长定义的形式参数会作为元组存在, 接收不定长数量的参数传入
def user_info(*args):
    print(f"args的参数类型是{type(args)},内容是{args}")

user_info("小红", 18, "女")

# 关键字不定长参数
def user_info(**kwargs):
    print(f"kwargs的参数类型是{type(kwargs)},内容是{kwargs}")

user_info(name="小红", age=18, gender="女")

# 函数作为参数传人
def test_func(compute):
    result = compute(1, 2)
    print(f"计算结果是{result}")

def compute(x, y):
    return x + y

test_func(compute)