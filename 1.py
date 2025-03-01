import pandas as pd

data = pd.read_csv('Travel_data.csv')
print(data)
print(data.dtypes)
pd.to_datetime(data['出发时间'])
data["出发时间"] = data["出发时间"].astype("datetime64[ns]")
df = data["地点"].value_counts()
df = df.head(5)
df
import matplotlib.pyplot as plt

x = df.index
y = df.values
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 6))
plt.bar(x, y, color="g")
plt.title("最热门的五大旅游城市", fontsize=20)
plt.xlabel("地点", fontsize=18)
plt.ylabel("旅游文章数量")
plt.tick_params(labelsize=14)
plt.xticks(rotation=90)
for a, b in zip(x, y):
    plt.text(a, b + 10, b, ha='center', va='bottom', fontsize=10)
plt.show()
df1 = data['地点'].value_counts()
y = df1.values
y = y / sum(y)
plt.figure(figsize=(7, 7))
plt.title("结伴人数占比", fontsize=15)
patches, l_text, p_text = plt.pie(y, labels=df1.index, autopct='%.1f %%', colors='bygr', startangle=90)
for i in p_text:
    i.set_size(15)
    i.set_color('w')
for i in l_text:
    i.set_size(15)
    i.set_color('r')
plt.legend()
plt.show()
plt.figure(figsize=(10, 6))
plt.hist(data["人均费用"], bins=20, edgecolor='k', alpha=0.5)
plt.show()
from scipy.stats import norm

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)
n, bins, patches = ax1.hist(data["旅行天数"], bins=100, color='m')
ax1.set_ylabel("人均费用", fontsize=15)
ax1.set_xlabel("旅行天数", fontsize=15)
ax1.set_title("频率分布图", fontsize=20)
y = norm.pdf(bins, data["旅行天数"].mean(), data["旅行天数"].std())
ax2 = ax1.twinx()
ax2.plot(bins, y, "b--")
ax2.set_ylabel("概率分布", fontsize=15)
plt.show()
