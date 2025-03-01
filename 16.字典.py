# 1.字典的定义语法
my_dict = {"name": "python", "age": 18, "sex": "男"}
# 空字典
my_dict2 = {}
my_dict3 = dict()

# 2.从字典中基于Key获取Value
my_dict = {"name": "python", "age": 18, "sex": "男"}
name = my_dict["name"]
print(name)  # python

# 3.定义嵌套字典
my_dict = {
    "name": "python",
    "age": 18,
    "address": {
        "province": "北京",
        "city": "北京"
    }
}
# 取出嵌套字典中的值
province = my_dict["address"]["province"]
print(province)

# 新增元素
my_dict4 = {"name": "python", "age": 18}
my_dict4["address"] = "北京"
print(my_dict4) # {'name': 'python', 'age': 18, 'address': '北京'}

# 更新元素
my_dict4["age"] = 20
print(my_dict4) # {'name': 'python', 'age': 20, 'address': '北京'}

# 删除元素
name = my_dict4.pop("name") # 删除name对应的值并返回
print(f"被删除的内容是{name}") # 被删除的内容是python
del my_dict4["age"]
print(my_dict4) # {'address': '北京'}

# 清空字典
my_dict4.clear()
print(my_dict4)

# 获取字典的所有key
keys = my_dict.keys()
print(keys) # dict_keys(['name', 'age', 'address'])

# 遍历字典
my_dict = {"name": "python", "age": 18, "sex": "男"}
for key in my_dict.keys():
    print(f"字典的Key是{key}")
    print(f"字典的Value是{my_dict[key]}")
    print()
# 方式2（结果同上相同）
for key in my_dict:
    print(f"字典的Key是{key}")
    print(f"字典的Value是{my_dict[key]}")
    print()