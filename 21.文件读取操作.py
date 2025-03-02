# open("文件路径", mode, encodeing)
# mode: r: 只读的方式打开文件
#       w: 只写的方式打开文件，如果文件不存在，则创建文件，如果文件存在，则覆盖文件
#       a: 只写的方式打开文件，如果文件不存在，则创建文件，如果文件存在，则追加内容
f = open("./文件测试/1.txt" , "r", encoding="utf-8")

# 读取文件内容(可以传入参数，代表要读取多少个字节，如果不传入则代表全部读取)
content = f.read()
print(content)

# 读取一行
# 由于上边的read()方法，读取了全部内容，所以这里只能读取空字符串
content = f.readline()
print(f"第一行数据是{content}")

# 通过for循环读取每一行内容
for line in f:
    print(f"每一行的内容是：{line}")

# 关闭文件
f.close()

# with open() as f:语句
with open("./文件测试/1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"每一行的内容是：{line}")
    # 程序会自动关闭文件，所以这里不需要再写f.close()