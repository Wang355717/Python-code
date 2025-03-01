"""
一种可以容纳多份数据的数据类型，容纳的每一份数据称为1个元素。
每个元素可以是任意类型的数据，如字符串、数字。布尔等。
数据容器分为5类：
    列表(list)、元组(tuple)、字符串(str)、集合(set)、字典(dict)
"""
# 列表（定义、下标索引、常用操作）
"""
    1.特点：
        1.可以容纳多个元素
        2.可以容纳不同类型的元素
        3.数据是有序存储的（有下标序号）
        4.运行重复数据存在
        5.可以修改（增加或删除元素等）
    2.注意：
    1.列表一次可以存储多个数据
    2.可以为不同的数据类型
    3.支持嵌套
    4.列表的索引是从0开始的
    5.通过下标取列表的值一定不要超过列表的范围
"""
# 定义语法
# [元素1, 元素2, 元素3,.......]
my_list = ['穷查查', 20, 180.5, True, ['李哈哈', 20]]
print(my_list)
print(type(my_list))

# 下标索引
# 取出列表的第一个值
print(my_list[0])
# 取列表里面嵌套列表的第一个值
print(my_list[4][0])

# 列表的常用操作
# 1、查找某个元素在列表中的索引值 ，同时返回该数据在列表中的索引号,
# 如果被查找的元素不在，则会报错
# 语法：列表名.index(要查找的元素)
print(my_list.index(20))

# 2、修改特定位置（索引）的元素值
# 语法：列表名[下标] = 新值
my_list[1] = 21
print(f"修改后的列表是{my_list}")

# 3、在制定的下标插入新元素
# 语法：列表名.insert(下标, 元素)，在指定的下标位置，插入指定的元素
my_list.insert(1, "有本")     # 在下标为1的位置插入值之后，后边的下标会自动增加
print(f"插入后的列表是{my_list}")

# 4、追加元素
# 语法：列表名.append(元素)，将指定的元素，追加到列表的尾部
my_list.append(4)
print(f"追加后的列表是{my_list}")
# 追加多个元素
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(f"追加多个数据后的列表是{my_list}")


my_list = ['java', 'python', 'javascript', 'C++']
# 删除指定下标的元素
# 语法1：del 列表名[下标]
# 语法2：列表名.pop(下标)   同时返回被删除的结果
del my_list[2]
print(f"删除指定元素后的列表是{my_list}")

my_list = ['java', 'python', 'javascript', 'C++']
element = my_list.pop(2)
print(f"通过pop方法取出内容后的列表是{my_list}，被删除的是{element}元素")


my_list = ['java', 'python', 'javascript', 'C++', 'python']
# 5、删除列表中指定元素的所有匹配项
my_list.remove('python')
print(f"删除指定元素后的列表是{my_list}")


# 6、清空列表
my_list.clear()
print(f"清空列表后的列表是{my_list}")


# 7、统计某元素在列表的数量
my_list = [1, 1, 1, 2, 3]
print(f"列表中1的数量是:{my_list.count(1)}")


my_list = [1, 1, 1, 2, 3]
# 8、统计列表的中全部的元素数量
print(f"列表中元素的数量是:{len(my_list)}")


# 9、遍历列表
# while遍历
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# for遍历
my_list = [1, 8, 5, 6, 3]
for item in my_list:
    print(item, end=" ")

