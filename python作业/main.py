import requests
from bs4 import BeautifulSoup
import time

def fetch_novel(url):
    # 设置请求头，避免被反爬
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    # 获取主页内容
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print(f"无法访问主页，状态码: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取小说名字
    try:
        novel_name = soup.find('div', class_='lazy').find('img')['alt'].strip()
    except AttributeError:
        print("无法找到小说名称，请检查页面结构")
        return
    print(f"小说名字: {novel_name}")

    # 获取章节列表
    chapter_list = []
    try:
        chapter_area = soup.find('div', class_='listmain')  # 查找章节区域
        for chapter in chapter_area.find_all('a'):
            chapter_title = chapter.text.strip()
            chapter_link = url.rstrip('/') + chapter['href']  # 拼接完整的章节链接
            chapter_list.append((chapter_title, chapter_link))
    except AttributeError:
        print("无法找到章节列表，请检查页面结构")
        return

    print(f"共发现 {len(chapter_list)} 个章节")

    # 创建以小说名字命名的文本文件
    with open(f"{novel_name}.txt", "w", encoding="utf-8") as file:
        # 遍历所有章节并写入内容
        for i, (title, link) in enumerate(chapter_list):
            print(f"正在爬取第 {i+1}/{len(chapter_list)} 章: {title}")
            chapter_content = fetch_chapter_content(link, headers)
            if chapter_content:
                file.write(title + "\n\n")
                file.write(chapter_content + "\n\n")
                time.sleep(1)  # 避免爬取过快被封禁
            else:
                print(f"章节 {title} 无法抓取，跳过。")

    print(f"小说《{novel_name}》爬取完成，已保存到 {novel_name}.txt")


def fetch_chapter_content(url, headers):
    # 获取章节页面内容
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print(f"无法访问章节页面: {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取章节正文
    try:
        content_area = soup.find('div', class_='content')  # 章节内容容器
        content = "\n".join([p.text.strip() for p in content_area.find_all('p')])  # 合并段落
    except AttributeError:
        print(f"未找到章节内容: {url}")
        return None

    return content


if __name__ == "__main__":
    # 小说主页 URL
    novel_url = "https://www.ixiaoshu.com/b/605496/"
    fetch_novel(novel_url)
