money = 5000000
uname = input("请输入您的姓名:")

# 查询余额函数
def query():
    print("--------------查询--------------")
    print(f"{uname}您好，您的余额剩余{money}元")

# 存款
def save():
    global money
    print("请输入要存的钱数:", end="")
    money += int(input(""))
    print(f"{uname}您好，当前余额为{money}元")

# 取钱函数
def take():
    global money
    print("请输入要取的钱数:", end="")
    money -= int(input(""))
    print(f"{uname}您好，当前余额为{money}元")

while True:
    print(f"{uname}您好，欢迎来到银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    num = int(input("请输入您的选择:"))
    if num == 1:
        query()
    elif num == 2:
        save()
    elif num == 3:
        take()
    elif num == 4:
        break
    else:
        print("输入的数据有误，程序退出")
        break
