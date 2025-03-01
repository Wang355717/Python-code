my_str = "python and itcast"

# 1.通过下标取值
# 取y的值
value1 = my_str[1]
value2 = my_str[-16]
print(value2)

# 2.index方法
# 查看and的下标
index = my_str.index("and")
print(f"and的下标是{index}")

# 3.replace方法
new_str = my_str.replace("and", "&")
print(f"替换后的字符串是:{new_str}")

# 4.split方法
list1 = my_str.split(" ")
print(f"分割后的列表是：{list1}")

# 5.strip方法
my_str = "  python and itcast  "
new_str = my_str.strip()    # 不传入参数，默认去除前后空格
print(f"去除前后空格的字符串是:{new_str}")

# 5.1strip带参数的方法
my_str = "12python and itcast21"
new_str = my_str.strip("12")
print(f"去除前后空格的字符串是:{new_str}")

# 6.count方法
my_str = "pythonit and itcast"
count = my_str.count("it")
print(f"it出现的次数是:{count}")

# 7.len方法
print(f"字符串的长度是:{len(my_str)}")


