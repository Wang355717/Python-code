# w模式：文件有，会覆盖文件内容，如果文件没有，则创建文件
f = open("./文件测试/test.txt", "w", encoding="utf-8")

# write写入文件内容
f.write("Hello World")

# close关闭文件
f.close()   # 内置flush功能

# 追加写入模式
f = open("./文件测试/test.txt", "a", encoding="utf-8")
f.write("你好世界")
f.close()