def display_java_version():
    # 使用原始字符串处理路径
    command_output = r"""C:\Users\MistL>java -version
java version "21.0.2" 2024-01-16 LTS
Java(TM) SE Runtime Environment (build 21.0.2+13-LTS-58)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.2+13-LTS-58, mixed mode, sharing)

C:\Users\MistL>"""

    # 打印文本
    print(command_output)

# 调用函数
display_java_version()