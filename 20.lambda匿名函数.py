def test_func(compute):
    result = compute(1, 2)
    print(f"计算结果是{result}")

test_func(lambda x, y: x + y)