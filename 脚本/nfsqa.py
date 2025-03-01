# cron "0 10 2,23 * * *"
# const $ = new Env('农夫山泉抽水')
# 农夫山泉小程序抓包apitoken
# nfsqtoken=apitoken多账号用&
# 内置了一些坐标 默认随机抽奖地区 如果需要指定变量provice_name 值为省份


import requests
import json
from datetime import datetime
import urllib3
import time
import generate_mapdata
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 获取环境变量并检查是否为空
nfsqtoken = os.getenv("nfsqtoken")
if not nfsqtoken:
    print("环境变量 'nfsqtoken' 未设置或为空，请检查配置。")
    exit(1)  # 退出程序，避免后续逻辑执行失败

account_tokens = nfsqtoken.split("&")

provice_name = os.getenv("provice_name", "默认省份")  # 如果未设置，则使用默认值

headers_template = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf254010d) XWEB/11607'
}


def get_tasks(headers):
    print(f"开始获取任务")

    res1 = requests.get(
        "https://gateway.jmhd8.com/geement.marketingplay/api/v1/task?pageNum=1&pageSize=10&task_status=2&status=1&group_id=24121016331837",
        headers=headers,
        verify=False
    )

    if res1.status_code != 200:
        print(f"请求失败，状态码: {res1.status_code}")
        return []

    rw = res1.json()
    if not rw.get("data"):
        print("没有任务数据")
        return []

    tasks = []
    for task in rw["data"]:
        task_name = task["name"]
        task_id = task["id"]
        reward_name = task["reward"][0]["relationship_name"]
        reward_count = task["reward"][0]["reward_count"]
        allow_complete_count = task["allow_complete_count"]
        complete_count = task["complete_count"]
        task_status = "有效" if task["task_status"] == 2 else "无效"

        print(f"任务名称: {task_name}")
        print(f"任务ID: {task_id}")
        print(f"奖励名称: {reward_name}")
        print(f"每次奖励数量: {reward_count}")
        print(f"允许完成次数: {allow_complete_count}")
        print(f"已完成次数: {complete_count}")
        print(f"任务状态: {task_status}")
        print("-" * 50)

        tasks.append({
            "task_name": task_name,
            "task_id": task_id,
            "allow_complete_count": allow_complete_count,
            "complete_count": complete_count,
            "reward_count": reward_count,
            "task_status": task_status
        })

    return tasks


def task(task_name, task_id, allow_complete_count, complete_count, headers):
    print(f"开始执行任务: {task_name}")
    for i in range(complete_count, allow_complete_count):
        print(f"正在执行第 {i + 1} 次任务...")

        # 动态获取时间
        formatted_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        res = requests.get(
            f"https://gateway.jmhd8.com/geement.marketingplay/api/v1/task/join?action_time={formatted_date}&task_id={task_id}",
            headers=headers,
            verify=False
        )

        # 解析任务执行结果
        res_data = res.json()
        if res.status_code == 200 and res_data.get('success'):
            print(f"第 {i + 1} 次任务成功: {res_data.get('msg')}")
        else:
            print(f"第 {i + 1} 次任务失败: {res_data.get('msg') if res_data.get('msg') else '未知错误'}")
        print("-" * 50)


def gametask(headers, mapdata):
    win_date = datetime.now().strftime('%Y-%m-%d')

    gurl = f"https://thirtypro.jmhd8.com/api/v1/nongfuwater/snake/checkerboard/lottery"

    # 定义最大尝试次数（可根据需求调整）
    max_attempts = 10  # 假设最多尝试 10 次
    for attempt in range(1, max_attempts + 1):
        print(f"正在玩第 {attempt} 次游戏...")

        # 发送请求
        resg = requests.post(gurl, headers=headers, verify=False, json=mapdata)
        resg_data = resg.json()
        # print(resg_data)

        # 检查请求是否成功
        if resg.status_code != 200:
            print(f"请求失败，状态码: {resg.status_code}")
            print(resg.json())  # 打印错误信息
            break

        # 检查返回的数据
        if not resg_data.get("success", False):
            print(f"游戏失败: {resg_data.get('msg', '未知错误')}")

            # 如果提示当天棋盘格次数已用尽，则退出循环
            if "当天的棋盘格次数已用尽" in resg_data.get("msg", ""):
                break
            continue

        # 检查是否有中奖信息
        if "data" in resg_data and resg_data["data"] is not None and "prizedto" in resg_data["data"]:
            prize_info = resg_data["data"]["prizedto"]

            # 提取奖品名称和等级
            prize_name = prize_info.get("prize_name", "未知奖品")
            prize_level = prize_info.get("prize_level", "未知等级")

            # 如果中奖，打印中奖信息
            print(f"恭喜！抽中奖品：{prize_name}（等级：{prize_level}）")

            # 检查资格卡券不足的情况
            if "资格卡券不足" in resg_data.get("msg", ""):
                print("资格卡券不足，抽奖结束。")
                break
        else:
            print("未中奖或返回数据格式错误")

    print("游戏结束。")

print(1,2 ,sep=",")
def choujiang(headers, mapdata):
    # print(f"当前抽奖城市为{mapdata["provice_name"] }")

    url = "https://gateway.jmhd8.com/geement.marketinglottery/api/v1/marketinglottery"
    attempt = 0
    while True:
        attempt += 1
        print(f"第 {attempt} 次抽奖开始...")

        res4 = requests.session().post(url, headers=headers, json=mapdata, verify=False)

        if res4.status_code != 200:
            print(f"请求失败，状态码: {res4.status_code}")
            print(res4.json())
            break

        res4_data = res4.json()

        if not res4_data.get("success", False):
            print(f"抽奖失败：{res4_data.get('msg', '未知错误')}")
            break

        if "data" in res4_data and "prizedto" in res4_data["data"]:
            prize_info = res4_data["data"]["prizedto"]

            prize_name = prize_info.get("prize_name", "未知奖品")
            prize_level = prize_info.get("prize_level", "未知等级")

            print(f"第 {attempt} 次抽奖结果: 奖品名称: {prize_name}, 等级: {prize_level}")

            if "资格卡券不足" in res4_data.get("msg", ""):
                print("资格卡券不足，抽奖结束。")
                break

            if prize_name and prize_level:
                print(f"恭喜！抽中奖品：{prize_name}（等级：{prize_level}）")
        else:
            print("未中奖或返回数据格式错误")

        time.sleep(2)


def main():
    mapdata = generate_mapdata.generate_mapdata(provice_name)
    print(f"账号数量: {len(account_tokens)}")
    for token in account_tokens:
        print(f"开始执行账号: {token}")

        headers = headers_template.copy()
        headers['apitoken'] = token

        tasks = get_tasks(headers)

        for task_data in tasks:
            if task_data["task_status"] == "有效" and task_data["complete_count"] < task_data["allow_complete_count"]:
                task(
                    task_name=task_data["task_name"],
                    task_id=task_data["task_id"],
                    allow_complete_count=task_data["allow_complete_count"],
                    complete_count=task_data["complete_count"],
                    headers=headers
                )
            else:
                print(f"任务: {task_data['task_name']} 无需执行或已完成")
                print("-" * 50)

        gametask(headers, mapdata)

        choujiang(headers, mapdata)


if __name__ == "__main__":
    main()
