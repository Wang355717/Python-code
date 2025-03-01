# 1、布尔类型和比较运算符
# 布尔类型定义
bool_1 = True
bool_2 = False
print(f"bool_1的类型是{type(bool_1)},bool_1的类型是{type(bool_2)}")

# 比较运算符
# ==、 !=、 >、 <、 >=、 <=
num1 = 10
num2 = 5
print(f"num1 == num2的结果是{num1 == num2}")
print(f"num1 != num2的结果是{num1 != num2}")
print(f"num1 > num2的结果是{num1 > num2}")
print(f"num1 < num2的结果是{num1 < num2}")
print(f"num1 >= num2的结果是{num1 >= num2}")
print(f"num1 <= num2的结果是{num1 <= num2}")

# 2、if语句的基本格式
"""
    if 要判断的条件:
        条件成立时要执行的语句
"""
age = 18
if age >= 18:
    print("我已经成年了")
print("时间过的真快呀!")

# 3、if else语句
"""
if 条件:
    条件满足执行的代码
else:
    条件不满足执行的代码
"""
age2 = int(input("请输入您的年龄:"))
if age2 >= 18:
    print("我已经成年了")
else:
    print("我没有成年")

# 4、if elif else 语句
"""
if 条件1:
    条件1满足执行的代码
elif 条件2:
    满足1但不满足2执行的代码
.......
else:
    当条件都不满足执行的代码
"""

# 5、判断语句的嵌套
"""
if 条件1:
    条件1满足执行的代码
    if 条件2:
        满足条件1，
else:
    所有的条件都不满足执行的代码
"""

# 随机数字，如下代码随机生成1-10之间的数字
import random
num = random.randint(1, 10)
