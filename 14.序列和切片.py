# 1、对list进行切片，从1开始，4结束，步长为1
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[1:4]) # 步长默认是1可以不写

# 2、对tuple切片，从头开始，到最后结束，步长为1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(my_tuple[:])

# 3、对str切片，从头开始，到最后结束，步长为2
my_string = "0123456"
print(my_string[::2])

# 4、对str切片，从头开始，到最后结束，步长为-1
my_string = "0123456"
print(my_string[::-1])