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