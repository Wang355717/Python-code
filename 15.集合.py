# 1.集合的定义语法
my_set = {"python", "java", "c++", "python", "java", "c++", "python", "java", "c++"}
print(f"my_set的内容是{my_set}，他的数据类型是{type(my_set)}")

# 2.集合的添加元素
my_set = {"python", "java", "c++", "python", "java"}
my_set.add("python")
my_set.add("嘿嘿嘿")
print(f"my_set添加元素后是：{my_set}")

# 3.移除元素
my_set = {"python", "java", "c++", "python", "java"}
my_set.remove("python")
print(f"my_set移除元素后是：{my_set}")  # my_set移除元素后是：{'c++', 'java'}

# 4.随机取出一个元素
my_set = {"python", "java", "c++"}
element = my_set.pop()
print(f"my_set随机取出一个元素是：{element}")  # my_set随机取出一个元素是：c++

# 5.清空集合
my_set = {"python", "java", "c++"}
my_set.clear()
print(f"my_set清空集合后是：{my_set}")  # my_set清空集合后是：set()

# 6.取出集合的差集   (集合1有而集合2没有)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set1和set2的差集是：{set3}")  # set1和set2的差集是：{2, 3}

# 7.消除两个集合的差集 (在集合1内，删除和集合2相同的元素)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"set1和set2的差集消除后是：{set1}")  # set1和set2的差集消除后是：{2, 3}
print(set1)  # {2, 3}
print(set2)  # {1, 5, 6}

# 8.合并两个集合
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"set1和set2合并后是：{set3}")  # set1和set2合并后是：{1, 2, 3, 5, 6}

# 9.统计集合元素的数量
set1 = {1, 2, 3}
print(f"set1中元素的数量是：{len(set1)}")  # 、set1中元素的数量是：3

# 10.集合的遍历
set1 = {1, 2, 3}
for element in set1:
    print(element)