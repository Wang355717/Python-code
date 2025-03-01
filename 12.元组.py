# 元组 定义元组使用小括号，且使用逗号隔开各个数据，数据可以是不同的数据类型

# 1.定义
t1 = (1, "Hello", True)
t2 = ()  # 空元组
t3 = tuple()  # 空元组

print(f"t1的类型是:{type(t1)},内容是：{t1}")
print(f"t2的类型是:{type(t2)},内容是：{t2}")
print(f"t3的类型是:{type(t3)},内容是：{t3}")

# 2.定义单个元组
t4 = 1  # 单个元组后面必须加上逗号，否则类型将变为其他数据类型
print(f"t4的类型是:{type(t4)},内容是：{t4}")

# 3.元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是:{type(t5)},内容是：{t5}")

# 4.元组index查找方法
t6 = ("Java", "Python", "C++")
index = t6.index("Python")
print(f"Python的下标是：{index}")

# 5.元组count查找方法
t7 = ("Java", "Python", "C++", "Python")
count = t7.count("Python")
print(f"Python的个数是：{count}")

# 6.元组切片
t8 = ("Java", "Python", "C++", "Python")
print(f"t8切片后是：{t8[1:3]}")

# 7.len统计元组长度
print(f"t8的长度是：{len(t8)}")

