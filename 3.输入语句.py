# input输入语句 ，获取用户输入的信息
"""
    注意：
        1.input里面默认可以写提示语句
        2.input默认接收的是字符串类型的数据，如果想要得到整数类型的，就要进行数据类型转换
        如int类型
            int(变量名)
        3.数据类型转换可简写为：变量名 = int(input("提示信息"))
"""
name = input("请告诉我你是谁：")
print("我知道了，你是：%s" % name)
