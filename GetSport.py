import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import urllib.request, urllib.error  # 制定URL，获取网页数据
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import os
from tqdm import tqdm
from selenium.webdriver.edge.options import Options
# import undetected_chromedriver.v2 as uc
import random


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' has been created.")
    else:
        print(f"Folder '{folder_path}' already exists.")


# NO USE
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

OlympicsList = pd.read_csv("./Olympics_event/olympic_games.csv")['Olympic Game']

# OlympicsList=['st-louis-1904']
# for Olympics in OlympicsList['Olympic Game']:
for Olympics in OlympicsList:
    print(Olympics)
    events = []
    while events ==[]:
        # 启动Selenium浏览器（需要安装ChromeDriver或者其他浏览器驱动）
        # 配置 Edge 浏览器选项
        options = Options()
        options.add_argument("user-data-dir=/Users/raymondlo/Library/Application Support/Microsoft Edge/Default")  # 替换为你的实际路径

        # 启动 Edge 浏览器并加载配置文件
        driver = webdriver.Edge(options=options)

        # 打开网页
        url = "https://olympics.com/en/olympic-games/" + Olympics + "/results"
        driver.get(url)
        print(url)

        # 设置滚动次数和每次滚动后的等待时间
        scroll_pause_time = 2  # 每次滚动后等待2秒
        total_scrolls = 5  # 总共滚动5次

        # 获取页面的高度
        last_height = driver.execute_script("return document.body.scrollHeight")

        for i in range(total_scrolls):
            # 滚动到页面底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 等待页面加载
            time.sleep(scroll_pause_time)

            # 获取新的页面高度，并检查是否到达了页面底部
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # 显式等待页面加载完成
        # wait = WebDriverWait(driver, 30)
        # 增加等待时间，确保页面加载完毕并显示Cookie弹窗
        for i in tqdm(range(3)):
            time.sleep(1)  # 等待5秒，可根据实际情况调整

        # 处理 Cookie 弹窗 如果设置了浏览器用户配置文件就无需点击Cookie弹窗
        # try:
        #     # 等待并点击 "Yes, I am happy" 按钮
        #     accept_cookies_button = WebDriverWait(driver, 15).until(
        #         EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        #     )
        #     accept_cookies_button.click()
        #     print("已接受Cookie弹窗")
        #
        #     wait = WebDriverWait(driver, 10)
        # except Exception as e:
        #     print("未找到或无法点击 Cookie 弹窗:", e)
        #
        # time.sleep(30)
        # 增加等待时间，确保页面加载完毕
        # for i in tqdm(range(10)):
        #     time.sleep(1)

        try:
            # 获取页面源代码
            html = driver.page_source

            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            # Find all the disciplines (sports events)
            # t = soup.find_all("section", {"data-cy": "disciplines-list"})
            # print(t

            disciplines = soup.find_all("a", {"data-cy": "disciplines-item"})

            print(disciplines)
            # Extract the name and URL of each discipline

            for discipline in tqdm(disciplines):
                event_name = discipline.text.strip()
                print(event_name)
                event_url = discipline['href']
                # 使用正则表达式提取最后的项目名称
                event_EN_name = re.search(r'/([^/]+)$', event_url).group(1)
                events.append(
                    {"Event Name": event_name, "Event English Name": event_EN_name, "URL": "https://olympics.com" + event_url})

            # Create a DataFrame to organize the events
            df = pd.DataFrame(events)
            folder = "./Olympics_event"
            create_folder_if_not_exists(folder)
            # Save the data to a CSV file
            df.to_csv(folder + "/" + Olympics + "_events.csv", index=False)

            # Display the data
            print(df)
        finally:
            # 无论成功与否，都会执行此处，确保浏览器关闭
            driver.quit()
            print("浏览器已关闭")

    print(events)