# while语句
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}\t", end='')
        j += 1
    i += 1
    print()

# for语句
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end='')
    print()
