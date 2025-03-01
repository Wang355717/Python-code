## Python常见的数据容器

### 一、list（列表）

>1. 列表中的每一项数据都称之为`元素`
>2. 元素的数据类型`没有限制`
>3. 允许数据重复
>4. 可以容纳不用的数据类型

#### 1.1、定义语法

```python
# 列表名 = [元素1, 元素2, 元素3, ....]
```

#### 1.2、列表嵌套

```python
# 列表名 = [ [元素1, 元素2, 元素3], [元素4, 元素5, 元素6], ....]
```

#### 1.3、列表的下标取出对应的值

```python
# 列表名 = [元素1, 元素2, 元素3]
# 列表名[下标索引]  从前向后从0开始，每次+1，	从后向前从-1开始，每次-1
#通过下标索引取数据，一定不要超出索引的范围，否则会报错 
```

#### 1.4、取嵌套列表的元素

```python
# 列表名 = [ [元素1, 元素2, 元素3], [元素4, 元素5, 元素6] ]
元素6 = 列表名[1][2]
```

#### 1.5、列表的方法

| 编号 | 使用方式                  | 作用                                     |
| :--: | ------------------------- | ---------------------------------------- |
|  1   | `列表.append(元素)`       | 向列表中追加一个元素                     |
|  2   | `列表.extend(容器)`       | 将数据容器的内容依次取出，追加到列表尾部 |
|  3   | `列表.insert(下标，元素)` | 在指定下标处插入指定元素                 |
|  4   | `del 列表[下标]`          | 删除列表指定下标元素                     |
|  5   | `列表.pop(下标)`          | 删除列表指定下标元素                     |
|  6   | `列表.remove(元素)`       | 从前向后，删除此元素第一个匹配项         |
|  7   | `列表.clear()`            | 清空列表                                 |
|  8   | `列表.count(元素)`        | 统计元素在列表出现的次数                 |
|  9   | `列表.index(元素)`        | 查找此元素的下标，找不到报ValueError     |
|  10  | `len(列表)`               | 统计容器内有多少的元素                   |



### 二、tuple（元组）

>1. 元组只有一个数据，这个数据后面要添加逗号
>2. 元组的数据不可以修改
>3. 支持for循环

#### 2.1、定义语法

```python
# 元组名 = (元素1, 元素2, 元素3, ....)
```

#### 2.2、定义单个元组

```python
# 元组名 = ("hello", )   # 必须有逗号，否则不是元组类型
```

#### 2.3、元组嵌套

```python
# 元组名 = ((元素1, 元素2, 元素3), (元素4, 元素5, 元素6))
```

#### 2.4、元组的下标取出对应的值

```python
# 元组名 = (元素1, 元素2, 元素3)
# 元组名[下标索引]  从前向后从0开始，每次+1，	从后向前从-1开始，每次-1
#通过下标索引取数据，一定不要超出索引的范围，否则会报错 
```

#### 2.5、取嵌套元组元素

>同列表方法相同

#### 2.6、元组的方法

| 编号 | 方法                 | 作用                                 |
| :--: | -------------------- | ------------------------------------ |
|  1   | `元组名.index(元素)` | 查找此元素的下标，找不到报ValueError |
|  2   | `元组名.count(元素)` | 统计元素在列表出现的次数             |
|  3   | `len(元组)`          | 统计容器内有多少的元素               |



### 三、str（字符串）

>1. <font color="red">只可以存储字符串</font>
>2. 长度任意
>3. 支持下标索引
>4. 允许重复字符串存在
>5. <font color="red">不可以修改</font>
>6. 支持for循环

#### 3.1、定义语法

```python
my_str = "python and itcast"
```

#### 3.2、通过下标取值

```python
# y的下标为：
value1 = my_str[1]
value2 = my_str[-16] # 空格也算一个字符
```

#### 3.3、index方法

```python
# 查看and的下标
value = my_str.index("and")
```

#### 3.4、replace替换方法

```python
# 语法：字符串.replace(字符串1, 字符串2)
# 功能：将字符串1的全部替换为字符串2，不会修改字符串本身，而是得到一个新的字符串
my_str = "python and itcast"
new_str = my_str.replace("and", "&")
print(f"替换后的字符串是:{new_str}")	# 替换后的字符串是:python & itcast
```

#### 3.5、split分割字符串

```python
# 语法：字符串.split(分割符字符串)
# 功能：按照指定的分隔符，将字符串划分为多个字符串，并存入列表对象中
# 注意：字符串本身不变，而是得到了一个列表对象
my_str = "python and itcast"
list1 = my_str.split(" ")
print(f"分割后的列表是：{list1}")	# 分割后的列表是：['python', 'and', 'itcast']
```

#### 3.6、strip字符串规整（取前后空格）

```python
my_str = "  python and itcast  "
new_str = my_str.strip()
print(f"去除前后空格的字符串是:{new_str}")	# 去除前后空格的字符串是:python and itcast

# 5.1strip带参数的方法
my_str = "12python and itcast21"
new_str = my_str.strip("12")
print(f"去除前后空格的字符串是:{new_str}")	# 去除前后空格的字符串是:python and itcast
```

#### 3.7、count统计字符串某字符出现的次数

```python
my_str = "pythonit and itcast"
count = my_str.count("it")
print(f"it出现的次数是:{count}")	# it出现的次数是:2
```

#### 3.8、len统计字符串的长度

```python
my_str = "pythonit and itcast"
print(f"字符串的长度是:{len(my_str)}")	# 字符串的长度是:19
```



### 四、序列

><font color="red">列表、元组、字符串均可以可视为序列。</font>

#### 4.1、切片

>切片：从一个序列中，取出一个子序列
>
>语法：<font color="red">序列[起始下标:结束下标:步长]</font>
>
>1. 起始下标表示从何处开始，可以留空，不写则表示从头开始
>2. 结束下标（不含）表示何处结束，可以留空，留空表示截取到结尾
>3. 步长表示依次取元素的间隔
>   - **步长1表示，一个一个取元素**
>   - **步长2表示，每次跳过1个元素取**
>   - **步长N表示，每次跳过N-1个元素取**
>   - **步长为负数表示，反向取（注意，起始下标和结束下标也要反向标记）**
>4. 此操作<font color="red">不会影响序列本身，而是会得到一个新的序列（列表、元组、字符串）</font>



### 五、set（集合）

>与其他唯一不同的地方在于<font color="red">不可以重复，并且内容是没有顺序的</font>

#### 5.1、基本语法

```python
# 定义集合字面量
{元素，元素，......元素}
# 定义集合变量
变量名称 = {元素，元素，......元素}
# 定义空集合
变量名称 = set()
```

#### 5.2、添加元素

```python
# 由于集合没有顺序，所以不支持下标访问元素，所以通过add方法来添加元素
my_set = {"python", "java", "c++", "python", "java"}
my_set.add("python")
my_set.add("嘿嘿嘿")
print(f"my_set添加元素后是：{my_set}")	# my_set添加元素后是：{'c++', 'python', 'java', '嘿嘿嘿'}		不可以重复，所以python没有添加上
```

#### 5.3、移除元素

```python
# remove方法
my_set = {"python", "java", "c++", "python", "java"}
my_set.remove("python")
print(f"my_set移除元素后是：{my_set}") # my_set移除元素后是：{'c++', 'java'}
```

#### 5.4、随机取出一个元素

```python
# pop方法
my_set = {"python", "java", "c++"}
element = my_set.pop()
print(f"my_set随机取出一个元素是：{element}") # my_set随机取出一个元素是：c++
```

#### 5.5、清空集合

```python
# clear方法
my_set = {"python", "java", "c++"}
my_set.clear()
print(f"my_set清空集合后是：{my_set}") # my_set清空集合后是：set()
```

#### 5.6、取2个集合的差集

```python
# 取出集合的差集  (集合1有而集合2没有)
# difference方法
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set1和set2的差集是：{set3}")  # my_set1和my_set2的差集是：{2, 3}
```

#### 5.7、消除2个集合的差集

```python
# difference_update方法
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"set1和set2的差集消除后是：{set1}") # set1和set2的差集消除后是：{2, 3}
print(set1) # {2, 3}
print(set2) # {1, 5, 6}
```

><font color="red">结果：集合1被修改，集合2不变</font>

#### 5.8、合并两个集合

```python
# union方法
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"set1和set2合并后是：{set3}")  # set1和set2合并后是：{1, 2, 3, 5, 6}
```

#### 5.9、统计集合元素数量

```python
# len方法
set1 = {1, 2, 3}
print(f"set1中元素的数量是：{len(set1)}")  # set1中元素的数量是：3
```

#### 5.10、集合的遍历

```python
# 由于集合没有下标，所以只能进行for循环遍历
set1 = {1, 2, 3}
for element in set1:
    print(element)
```



### 六、dict（字典）

#### 6.1、定义语法

```python
# 1.字典的定义语法
my_dict = {"name": "python", "age": 18, "sex": "男"}
# 空字典
my_dict2 = {}
my_dict3 = dict()
```

#### 6.2、从字典中基于Key获取Value

```python
my_dict = {"name": "python", "age": 18, "sex": "男"}
name = my_dict["name"]
print(name) # python
```

#### 6.3、字典的嵌套

```python
# 定义一个嵌套列表
my_dict = {
    "name": "python",
    "age": 18,
    "address": {
        "province": "北京",
        "city": "北京"
    }
}
# 取出嵌套字典中的值
province = my_dict["address"]["province"]
print(province)
```

#### 6.4、新增元素

```python
my_dict4 = {"name": "python", "age": 18}
my_dict4["address"] = "北京"
print(my_dict4) # {'name': 'python', 'age': 18, 'address': '北京'}
```

#### 6.5、更新字典元素

```python
my_dict4["age"] = 20
print(my_dict4) # {'name': 'python', 'age': 20, 'address': '北京'}
```

#### 6.6、删除元素

```python
name = my_dict4.pop("name") # 删除name对应的值并返回
print(f"被删除的内容是{name}") # 被删除的内容是python
del my_dict4["age"]
print(my_dict4) # {'address': '北京'}
```

#### 6.7、清空字典

```python
my_dict4.clear()
print(my_dict4)
```

#### 6.8、获取字典的所有Key

```python
keys = my_dict.keys()
print(keys) # dict_keys(['name', 'age', 'address'])
```

#### 6.9、遍历字典

```python
for key in my_dict.keys():
    print(f"字典的Key是{keys}")
    print(f"字典的Value是{my_dict[key]}")
```













