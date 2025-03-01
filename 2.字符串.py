# 1、字符串的定义方式
uname_str = '第一种定义方式'
print(type(uname_str))

uname_str2 = "第一种定义方式"
print(type(uname_str2))

uname_str3 = """
我是
小学生
"""
print(type(uname_str3))

# 2、字符串的拼接
print("穷哈哈" + "李查查")
# +号连接字符串变量或字符串字面量（无法和其他类型拼接）


# 3、字符串格式化
"""
占位符：
    1.%d整数类型
    2.%f浮点类型
    3.%s字符串类型
"""
# 3.1占位型拼接
name = "石工院"
message = "谁来%s谁后悔" % name
print(message)

# 3.2通过占位方式拼接字符串和数字
class_num = 3
avg_salary = 5000
message = "Python数据分析师，班级：%s班,平均工资：%s" % (class_num, avg_salary)
print(message)

name = "小王"
setup_year = 2003
height = 180.05
message = "我是%s,出生年是%d,身高是：%f" % (name, setup_year, height)
print(message)

# 字符串的快速格式化
"""
    1.不会理会数据类型
    2.不做精度控制
"""
message = (f"我是{name},出生年是{setup_year}，身高是{height}")
print(message)
