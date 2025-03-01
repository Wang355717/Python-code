# 1、while循环的语法
"""
    while 条件:   条件需要得到布尔类型
        条件成立一直做的事情

    规划好终止条件，否则将进入死循环
"""
# 求1-100的和
i = 0
num = 0
while i <= 100:
    num += i
    i += 1
print(num)

# import random
# num = random.randint(1, 100)
# count = 0
# flag = True
# while flag:
#     count += 1
#     guess_num = int(input("请输入你要猜的数字："))
#     if guess_num == num:
#         print("恭喜你猜对了")
#         flag = False
#     else:
#         if guess_num > num:
#             print("数字大了")
#         else:
#             print("数字小了")
# print(f"一共猜了{count}次")

# 2.while 循环的嵌套
"""
while 条件1:
    条件1满足，执行的语句
    条件1满足，执行的语句
    while 条件2:
        条件2满足，执行的语句
        条件2满足，执行的语句
"""

# 3.for循环的语法
"""
    for 临时变量 in 待处理数据集:
    循环满足条件执行的代码
"""

# 4.range 语法1 range(num)
"""
    for x in range(5):
    print(x)    # 0 1 2 3 4
"""

# range 语法2 range(num1, num2)
"""
    for x in range(1, 5):
    print(x)    从1开始，到5结束(不包括5)
"""

# range 语法3 range(num1, num2, step)
"""
    for x in range(5, 10, 2):
    print(x)    从1开始，到5结束(不包括5)数字间隔是2
    # 5 7 9
"""


# 5.for循环的嵌套

# 6.循环中断 continue 和 break
"""
    continue 跳出本次循环，直接进入下一次循环
    break 跳出整个循环，不再执行循环体(当前循环体)
"""

# 1-100之间有多少偶数
num = 100
count = 0
for i in range(1, num):
    if i % 2 == 0:
        count += 1
print(f"1-100中一共有{count}个偶数")
