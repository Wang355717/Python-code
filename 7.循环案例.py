import random

# 账户余额
money = 10000

for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效不满足{score}，不发工资")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}满足条件，发放工资1000元。公司账户余额为{money}元")
    else:
        print("对不起，账户余额不足，下个月再发")
        break
