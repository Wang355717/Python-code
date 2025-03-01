# 逻辑运算符

# and 左右两边都相等，才为真
a = 10
b = 10
if a == 10 and b == 10:
    print(f"{a}和{b}相等")

# or 左右两边只要有一个为真，则为真
if a == 10 or b == 20:
    print(f"{a}和{b}相等")

# not 取反
print(not 3 > 9) # True